const $ = window.$;
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    if ($('header').attr('class') === 'green') {
      console.log($('header').attr('class'));
      $('header').attr('class', 'red');
    } else {
      $('header').attr('class', 'green');
    }
  });
});
