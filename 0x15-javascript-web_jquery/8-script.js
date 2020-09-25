const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$(document).ready(function () {
  $.getJSON(url, function (json) {
    for (const i of json.results) {
      $('UL#list_movies').append(`<li>${i.title}</li>`);
    }
  });
});
