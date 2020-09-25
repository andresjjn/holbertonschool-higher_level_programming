const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$(document).ready(function () {
  $.getJSON(url, function (json) {
    $('DIV#hello').text(json.hello);
  });
});
