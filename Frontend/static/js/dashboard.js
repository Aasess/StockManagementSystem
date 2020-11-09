/* globals Chart:false, feather:false */

(function () {
    'use strict'
    feather.replace()
  })()

  const loader = document.querySelector('.loader');
  const content = document.querySelector('.display-content');
  
  function init() {
    setTimeout(() => {
      loader.style.opacity = 0;
      loader.style.display = 'none';
  
      content.style.display = 'block';
      setTimeout(() => (content.style.opacity = 1), 50);
    }, 1000);
  }
  
  init();
  
