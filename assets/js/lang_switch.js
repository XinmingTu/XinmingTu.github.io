document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('lang-toggle');
  if (!toggle) return;

  var enBtn = toggle.querySelector('.lang-en-btn');
  var zhBtn = toggle.querySelector('.lang-zh-btn');
  var saved = localStorage.getItem('lang') || 'en';

  function setLang(lang) {
    var enBlocks = document.querySelectorAll('.lang-en');
    var zhBlocks = document.querySelectorAll('.lang-zh');

    for (var i = 0; i < enBlocks.length; i++) {
      enBlocks[i].style.display = lang === 'en' ? '' : 'none';
    }
    for (var i = 0; i < zhBlocks.length; i++) {
      zhBlocks[i].style.display = lang === 'zh' ? '' : 'none';
    }

    enBtn.classList.toggle('active', lang === 'en');
    zhBtn.classList.toggle('active', lang === 'zh');
    localStorage.setItem('lang', lang);
  }

  setLang(saved);

  toggle.addEventListener('click', function () {
    var current = localStorage.getItem('lang') || 'en';
    setLang(current === 'en' ? 'zh' : 'en');
  });
});
