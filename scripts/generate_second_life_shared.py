"""Matched-task appendix; optionally import minimal records from the pinned eval repo.

python3 scripts/generate_second_life_shared.py --import-dir /path/to/eval/repo
Subsequent builds use only the checked-in snapshot; no model calls.
"""
import argparse
import html
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / 'assets/data/second-life-tb4/shared-task-records.json'
OUT = ROOT / 'assets/img/2026-08-28-second-life-agent-evals'
REVIEWERS = ['gpt-5-6-sol', 'glm-5-3-flash', 'glm-5-3', 'deepseek-v4p1-flash']
LABELS = ['GPT-5.6 Sol', 'GLM-5.3 Flash', 'GLM-5.3', 'DeepSeek V4.1 Flash']
SOURCES = ['fable-5.1', 'glm-5.3', 'gpt-5.6-sol']
NAMES = {'fable-5.1': 'Fable 5.1', 'glm-5.3': 'GLM-5.3', 'gpt-5.6-sol': 'GPT-5.6 Sol', 'gpt-6-astra': 'GPT-6 Astra'}
COMMIT = '6d99501ad21662cad4ef82c9089e15492d24e976'


def import_records(directory):
    head = subprocess.check_output(['git', '-C', str(directory), 'rev-parse', 'HEAD'], text=True).strip()
    assert head == COMMIT, 'Import requires the pinned experiment commit'
    records = []
    files = []
    for reviewer in REVIEWERS:
        single = (f'tbench4-glm-flash-complete-{reviewer}-single_pair.jsonl'
                  if reviewer == 'glm-5-3-flash' else f'tbench4-complete-{reviewer}-single_pair.jsonl')
        five = (f'tbench4-complete-{reviewer}-five_full.jsonl'
                if reviewer == 'glm-5-3-flash' else f'tbench4-all-mixed-five-{reviewer}.jsonl')
        for name in [single, five, f'tbench4-gpt6-source-{reviewer}-five_full.jsonl']:
            files.append(name)
            for line in (directory / 'results' / name).read_text().splitlines():
                row = json.loads(line)
                if name == single and row['condition'] not in {'single-full', 'pair-full'}:
                    continue
                keys = ['source_key', 'task_name', 'condition', 'trial_ids', 'gold_rewards',
                        'format_valid', 'predicted_reward', 'correct', 'preferred_success',
                        'selected_candidate', 'selected_success', 'candidate_a_predicted_reward',
                        'candidate_b_predicted_reward', 'usage']
                records.append(dict(reviewer=reviewer, **{k: row[k] for k in keys if k in row}))
    SNAPSHOT.write_text(json.dumps({'commit': COMMIT, 'files': files, 'records': records}, indent=2) + '\n')


def shared(rows, sources):
    sets = [{r['task_name'] for r in rows if r['source_key'] == source and r['condition'] == 'five-full'
             and r['reviewer'] == REVIEWERS[0]} for source in sources]
    return sorted(set.intersection(*sets))


def score(row):
    if not row['format_valid']:
        return False
    if row['condition'] == 'single-full':
        result = row['predicted_reward'] == row['gold_rewards'][0]
        assert result == row['correct']
        return result
    if row['condition'] == 'five-full':
        choice = row['selected_candidate']
        assert choice in range(1, 6)
        result = row['gold_rewards'][choice - 1] == 1
        assert result == row['selected_success']
        return result
    return row['preferred_success']  # Recorded selected-pair outcome, not exact classification.


def draw(rows, tasks, sources, panels, name):
    # Narrow, vertically stacked panels retain readable text on mobile.
    width, panel_height = 660, 148 + 48 * len(sources)
    height = 28 + len(panels) * panel_height
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">',
             '<title>Terminal-Bench 4.0: all available pools versus shared tasks</title>',
             '<desc>Each cell shows all available pools on top and the shared-task subset below. Counts and rates by reviewer and source; matching controls task identities, not trace contents or success mixtures.</desc>']
    def text(x, y, value, size=15, anchor='start'):
        parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="font-family:Arial,sans-serif;font-size:{size}px;fill:#20242d">{html.escape(value)}</text>')
    summary = []
    for p, (title, condition, negative) in enumerate(panels):
        top = 24 + p * panel_height
        text(8, top, title, 17)
        text(8, top + 22, 'Each cell: all available pools (top) / shared tasks only (bottom)', 13)
        for i, label in enumerate(LABELS):
            # Two-line headers avoid long-model-name collisions.
            words = label.rsplit(' ', 1) if len(label) > 13 else [label]
            for j, word in enumerate(words):
                text(220 + i * 123, top + 45 + j * 15, word, 13, 'middle')
        for s, source in enumerate(sources):
            y = top + 86 + s * 48
            text(8, y, NAMES[source])
            for i, reviewer in enumerate(REVIEWERS):
                available = [r for r in rows if r['source_key'] == source
                          and r['reviewer'] == reviewer and r['condition'] == condition
                          and (not negative or r['gold_rewards'] == [0])]
                matched = [r for r in available if r['task_name'] in tasks]
                assert len(matched) == len(tasks) * (2 if condition == 'single-full' and not negative else 1)
                for offset, (population, subset) in enumerate([('all', available), ('shared', matched)]):
                    n = len(subset)
                    wins = sum(score(r) for r in subset)
                    row_y = y - 7 + offset * 20
                    color = '#747d8b' if population == 'all' else '#4f68b3'
                    parts.append(f'<rect x="{166 + i * 123}" y="{row_y-14}" width="{108*wins/n:.2f}" height="19" rx="2" style="fill:{color};opacity:0.16"/>')
                    text(220 + i * 123, row_y, f'{wins}/{n} ({100*wins/n:.1f}%)', 13, 'middle')
                    summary.append(dict(panel=title, population=population, source=source, reviewer=reviewer, wins=wins, n=n))
        baseline_y = top + 86 + len(sources) * 48
        if condition == 'five-full':
            values = []
            for source in sources:
                subset = [r for r in rows if r['source_key'] == source
                          and r['reviewer'] == REVIEWERS[0] and r['condition'] == condition]
                matched = [r for r in subset if r['task_name'] in tasks]
                rates = [100*sum(sum(r['gold_rewards']) for r in group)/(5*len(group)) for group in (subset, matched)]
                values.append(f"{NAMES[source]} {rates[0]:.1f}% / {rates[1]:.1f}%")
            text(8, baseline_y, 'Uniform baseline (all / shared):', 13)
            text(8, baseline_y + 18, ' · '.join(values[:2]), 13)
            text(8, baseline_y + 36, ' · '.join(values[2:]), 13)
        else:
            text(8, baseline_y, 'Random binary guess: 50%' if condition == 'single-full' else 'Uniform selection: 50%', 13)
    parts.append('</svg>')
    (OUT / f'{name}.svg').write_text('\n'.join(parts) + '\n')
    return summary


def heatmap(rows, tasks, sources, panels, name):
    height = 90 + len(panels) * (105 + len(sources) * 45)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 {height}">',
           '<title>Terminal-Bench 4.0: identical task pool, different sources and reviewers</title>']
    def txt(x, y, label, size=14, anchor='start', color='#20242d'):
        svg.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="font-family:Arial,sans-serif;font-size:{size}px;fill:{color}">{html.escape(label)}</text>')
    def delta_color(delta):
        assert -1 <= delta <= 1
        end = (39,70,131) if delta >= 0 else (167,73,24)
        return '#%02x%02x%02x' % tuple(round(a+(b-a)*abs(delta)) for a,b in zip((243,243,243),end))
    txt(8, 20, f'Same {len(tasks)} tasks; color = percentage-point difference from random')
    for i, delta in enumerate([-1, -.5, 0, .5, 1]):
        x = 8 + i*128
        svg.append(f'<rect x="{x}" y="32" width="22" height="14" fill="{delta_color(delta)}"/>')
        txt(x+28,44,f'{delta*100:+.0f} pp' if delta else 'Random',12)
    for p, (title, condition, negative) in enumerate(panels):
        top = 85 + p * (105 + len(sources) * 45)
        txt(8, top, title, 17)
        for i, label in enumerate(LABELS):
            words = label.rsplit(' ', 1) if len(label) > 13 else [label]
            for j, word in enumerate(words):
                txt(219 + i * 123, top + 24 + 15*j, word, 13, 'middle')
        for s, source in enumerate(sources):
            y = top + 47 + s*45
            txt(8, y+24, NAMES[source])
            for i, reviewer in enumerate(REVIEWERS):
                subset = [r for r in rows if r['task_name'] in tasks and r['source_key'] == source and r['reviewer'] == reviewer and r['condition'] == condition and (not negative or r['gold_rewards'] == [0])]
                n, wins = len(subset), sum(score(r) for r in subset)
                rate = wins/n
                baseline = sum(sum(r['gold_rewards']) for r in subset)/(5*n) if condition == 'five-full' else .5
                delta = rate-baseline
                fill = delta_color(delta)
                svg.append(f'<rect x="{160+i*123}" y="{y}" width="118" height="41" rx="2" fill="{fill}"/>')
                ink = '#ffffff' if abs(delta) >= .65 else '#17243b'
                txt(219+i*123, y+17, f'{100*rate:.0f}% ({wins}/{n})', 14, 'middle', ink)
                txt(219+i*123, y+33, f'{100*delta:+.1f} pp' if abs(delta)>1e-10 else 'At random', 12, 'middle', ink)
        y = top+52+len(sources)*45
        if condition == 'five-full':
            values = []
            for source in sources:
                subset = [r for r in rows if r['task_name'] in tasks and r['source_key']==source and r['reviewer']==REVIEWERS[0] and r['condition']==condition]
                values.append(f"{NAMES[source]} {100*sum(sum(r['gold_rewards']) for r in subset)/(5*len(subset)):.1f}%")
            txt(8,y+12,'Uniform: '+' · '.join(values[:2]),13)
            txt(8,y+29,' · '.join(values[2:]),13)
        else:
            txt(8,y+12,'Random binary guess: 50%' if condition=='single-full' else 'Uniform selection: 50%',13)
    svg.append('</svg>')
    (OUT/f'{name}.svg').write_text('\n'.join(svg)+'\n')


def cost_table(rows):
    rates = {'glm-5-3': (1.4, .26, 4.4), 'glm-5-3-flash': (.15, .03, .5), 'deepseek-v4p1-flash': (.22, .007, .66)}
    result = []
    for reviewer, label in zip(REVIEWERS, LABELS):
        item = {'name': label}
        for condition, n in [('single',158), ('pair',79), ('five',79)]:
            subset = [r for r in rows if r['source_key'] in SOURCES and r['reviewer']==reviewer and r['condition']==condition+'-full']
            assert len(subset)==n
            costs=[]
            for r in subset:
                u=r['usage']
                reported=u.get('cost_usd') or 0
                if reviewer=='gpt-5-6-sol':
                    assert reported>0, 'Missing GPT dollar accounting'
                    cost=reported
                else:
                    inp,cached,out=(u[k] for k in ('input_tokens','cache_tokens','output_tokens'))
                    assert 0<=cached<=inp and out>=0
                    a,b,c=rates[reviewer]
                    cost=max(reported,((inp-cached)*a+cached*b+out*c)/1e6)
                costs.append(cost)
            item[condition]=f'{sum(costs)/n:.3f}'
            item[condition+'_total']=sum(costs)
            item[condition+'_n']=n
        result.append(item)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--import-dir', type=Path)
    args = parser.parse_args()
    if args.import_dir:
        import_records(args.import_dir)
    snapshot = json.loads(SNAPSHOT.read_text())
    assert snapshot['commit'] == COMMIT
    rows = snapshot['records']
    identities = [(r['reviewer'], r['source_key'], r['task_name'], r['condition'], tuple(r['trial_ids'])) for r in rows]
    assert len(identities) == len(set(identities)), 'Duplicate observations'
    # Every reviewer must see identical candidate order and labels for each case.
    cases = {}
    for r in rows:
        key = (r['source_key'], r['task_name'], r['condition'], tuple(r['trial_ids']))
        cases.setdefault(key, []).append(r)
    for group in cases.values():
        assert {r['reviewer'] for r in group} == set(REVIEWERS)
        assert len({tuple(r['gold_rewards']) for r in group}) == 1
    for r in rows:
        if r['condition'] != 'pair-full':
            continue
        assert sorted(r['gold_rewards']) == [0, 1]
        siblings = [x for x in rows if x['source_key'] == r['source_key'] and x['task_name'] == r['task_name'] and x['reviewer'] == r['reviewer']]
        anchors = [x for x in siblings if x['condition'] == 'single-full']
        five = [x for x in siblings if x['condition'] == 'five-full']
        assert len(anchors) == 2 and len(five) == 1
        assert {x['trial_ids'][0] for x in anchors} == set(r['trial_ids'])
        assert set(r['trial_ids']) <= set(five[0]['trial_ids'])
    three, four = shared(rows, SOURCES), shared(rows, SOURCES + ['gpt-6-astra'])
    assert len(three) == 6 and len(four) == 2
    panels = [('Single: classify success or failure', 'single-full', False),
              ('Pair: select the successful attempt', 'pair-full', False),
              ('Five: select any successful attempt', 'five-full', False)]
    first = draw(rows, three, SOURCES, panels, 'tb4-shared-tasks')
    second = draw(rows, four, SOURCES + ['gpt-6-astra'], [panels[-1]], 'tb4-shared-four')
    heatmap(rows, three, SOURCES, panels, 'tb4-shared-heatmap')
    heatmap(rows, four, SOURCES+['gpt-6-astra'], [panels[-1]], 'tb4-shared-four-heatmap')
    data = dict(commit=COMMIT, three_source_tasks=three, four_source_tasks=four, three_source_results=first, four_source_results=second)
    data['costs'] = cost_table(rows)
    (ROOT / '_data/second_life_shared.json').write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
