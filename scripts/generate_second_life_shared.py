"""Per-case TB4 snapshot: import, validation, shared-task lists and reviewer costs.

python3 scripts/generate_second_life_shared.py --import-dir /path/to/Agentic-Verification-Eval
reads the pinned commit with `git show`, so the checkout may be on any branch.
Without --import-dir, the checked-in snapshot is validated and
_data/second_life_shared.json is rebuilt. No model calls.
"""
import argparse
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / 'assets/data/second-life-tb4'
SNAPSHOT = SNAPSHOT_DIR / 'shared-task-records.json'
# Fixed presentation order: descending Five selection success over all 97 pools.
REVIEWERS = ['opus-5-5', 'gpt-5-6-sol', 'gpt-6-sol', 'glm-5-3-flash', 'glm-5-3', 'deepseek-v4p1-flash']
LABELS = ['Opus 5.5', 'GPT-5.6 Sol', 'GPT-6 Sol', 'GLM-5.3 Flash', 'GLM-5.3', 'DeepSeek V4.1 Flash']
FRONTIER = {'opus-5-5', 'gpt-6-sol'}
SOURCES = ['fable-5.1', 'glm-5.3', 'gpt-5.6-sol']
NAMES = {'fable-5.1': 'Fable 5.1', 'glm-5.3': 'GLM-5.3', 'gpt-5.6-sol': 'GPT-5.6 Sol', 'gpt-6-astra': 'GPT-6 Astra'}
COMMIT = '882fcc3349f161e9bfc3c1b92ab3c49b507480cc'
# Aggregate result files, copied unchanged from the pinned commit's results/ directory.
AGGREGATES = ['tbench4-complete-comparison.json', 'tbench4-complete-progress.json',
              'tbench4-glm-flash-complete-comparison.json', 'tbench4-glm-flash-complete-progress.json',
              'tbench4-gpt6-source-comparison.json', 'tbench4-gpt6-source-progress.json',
              'tbench4-pass-at-k.json', 'tbench4-frontier-comparison.json', 'tbench4-frontier-pass-at-k.json',
              'tbench4-frontier-single-failure-approval-ci.json', 'tbench4-frontier-progress.json']
FIELDS = ['source_key', 'task_name', 'condition', 'trial_ids', 'gold_rewards', 'format_valid', 'predicted_reward',
          'correct', 'preferred_success', 'selected_candidate', 'selected_success', 'candidate_a_predicted_reward',
          'candidate_b_predicted_reward', 'usage']


def git_show(directory, path):
    return subprocess.check_output(['git', '-C', str(directory), 'show', f'{COMMIT}:{path}'], text=True)


def result_files(reviewer):
    if reviewer in FRONTIER:
        return [f'tbench4-frontier-{reviewer}.jsonl']  # one audited file per reviewer, all 334 cases
    single = (f'tbench4-glm-flash-complete-{reviewer}-single_pair.jsonl'
              if reviewer == 'glm-5-3-flash' else f'tbench4-complete-{reviewer}-single_pair.jsonl')
    five = (f'tbench4-complete-{reviewer}-five_full.jsonl'
            if reviewer == 'glm-5-3-flash' else f'tbench4-all-mixed-five-{reviewer}.jsonl')
    return [single, five, f'tbench4-gpt6-source-{reviewer}-five_full.jsonl']


def import_records(directory):
    records, files = [], []
    for reviewer in REVIEWERS:
        names = result_files(reviewer)
        for name in names:
            files.append(name)
            for line in git_show(directory, f'results/{name}').splitlines():
                row = json.loads(line)
                # Single/Pair batch files also hold Five rows; each Five observation loads once, from its own file.
                if reviewer not in FRONTIER and name == names[0] and row['condition'] not in {'single-full', 'pair-full'}:
                    continue
                records.append(dict(reviewer=reviewer, **{k: row[k] for k in FIELDS if k in row}))
    SNAPSHOT.write_text(json.dumps({'commit': COMMIT, 'files': files, 'records': records}, indent=2) + '\n')
    for name in AGGREGATES:
        (SNAPSHOT_DIR / name).write_text(git_show(directory, f'results/{name}'))


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


def load_records():
    snapshot = json.loads(SNAPSHOT.read_text())
    assert snapshot['commit'] == COMMIT
    rows = snapshot['records']
    identities = [(r['reviewer'], r['source_key'], r['task_name'], r['condition'], tuple(r['trial_ids'])) for r in rows]
    assert len(identities) == len(set(identities)), 'Duplicate observations'
    # Every reviewer must see identical candidate order and labels for each case.
    cases = {}
    for r in rows:
        cases.setdefault((r['source_key'], r['task_name'], r['condition'], tuple(r['trial_ids'])), []).append(r)
    assert len(cases) == 334
    for group in cases.values():
        assert sorted(r['reviewer'] for r in group) == sorted(REVIEWERS)
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
    return rows


def cost_table(rows):
    rates = {'glm-5-3': (1.4, .26, 4.4), 'glm-5-3-flash': (.15, .03, .5), 'deepseek-v4p1-flash': (.22, .007, .66)}
    result = []
    for reviewer, label in zip(REVIEWERS, LABELS):
        item = {'key': reviewer, 'name': label}
        for condition, n in [('single', 158), ('pair', 79), ('five', 79)]:
            subset = [r for r in rows if r['source_key'] in SOURCES and r['reviewer'] == reviewer and r['condition'] == condition + '-full']
            assert len(subset) == n
            costs = []
            for r in subset:
                u = r['usage']
                reported = u.get('cost_usd') or 0
                if reviewer in FRONTIER or reviewer == 'gpt-5-6-sol':
                    assert reported > 0, 'Missing recorded dollar cost'
                    cost = reported
                else:
                    inp, cached, out = (u[k] for k in ('input_tokens', 'cache_tokens', 'output_tokens'))
                    assert 0 <= cached <= inp and out >= 0
                    a, b, c = rates[reviewer]
                    cost = max(reported, ((inp - cached) * a + cached * b + out * c) / 1e6)
                costs.append(cost)
            item[condition] = f'{sum(costs) / n:.3f}'
            item[condition + '_total'] = sum(costs)
            item[condition + '_n'] = n
        result.append(item)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--import-dir', type=Path)
    args = parser.parse_args()
    if args.import_dir:
        import_records(args.import_dir)
    rows = load_records()
    three, four = shared(rows, SOURCES), shared(rows, SOURCES + ['gpt-6-astra'])
    assert len(three) == 6 and len(four) == 2
    data = dict(commit=COMMIT, three_source_tasks=three, four_source_tasks=four, costs=cost_table(rows))
    (ROOT / '_data/second_life_shared.json').write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
