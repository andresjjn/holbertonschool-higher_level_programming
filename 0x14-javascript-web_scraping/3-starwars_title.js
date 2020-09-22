#!/usr/bin/node
const request = require('request');
const movie = process.argv[2];
if (!movie) {
  process.exit();
}
request(`https://swapi-api.hbtn.io/api/films/${movie}`, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const info = JSON.parse(body);
    console.log(info.title);
  } else {
    return console.log(err);
  }
});
