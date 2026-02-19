document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('lang-toggle');
  if (!toggle) return;

  var enBtn = toggle.querySelector('.lang-en-btn');
  var zhBtn = toggle.querySelector('.lang-zh-btn');

  // Priority: URL hash > localStorage > default 'en'
  var hash = window.location.hash.replace('#', '');
  var initial = (hash === 'en' || hash === 'zh') ? hash : (localStorage.getItem('lang') || 'en');

  function setLang(lang) {
    var enBlocks = document.querySelectorAll('.lang-en');
    var zhBlocks = document.querySelectorAll('.lang-zh');

    for (var i = 0; i < enBlocks.length; i++) {
      enBlocks[i].style.display = lang === 'en' ? 'block' : 'none';
    }
    for (var i = 0; i < zhBlocks.length; i++) {
      zhBlocks[i].style.display = lang === 'zh' ? 'block' : 'none';
    }

    enBtn.classList.toggle('active', lang === 'en');
    zhBtn.classList.toggle('active', lang === 'zh');
    localStorage.setItem('lang', lang);
    // Update URL hash without scrolling
    history.replaceState(null, '', '#' + lang);
  }

  setLang(initial);

  toggle.addEventListener('click', function () {
    var current = localStorage.getItem('lang') || 'en';
    setLang(current === 'en' ? 'zh' : 'en');
  });

  // Handle back/forward navigation
  window.addEventListener('hashchange', function () {
    var h = window.location.hash.replace('#', '');
    if (h === 'en' || h === 'zh') setLang(h);
  });
});
