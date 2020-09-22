#!/usr/bin/node
const request = require('request');
const movies = process.argv[2];
if (!movies) {
  process.exit().
}
let counter = 0;
request(movies, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const info = JSON.parse(body);
    for (let i = 0; i < info.results.length; i++) {
      for (const j in info.results[i].characters) {
        if (info.results[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          counter += 1;
        }
      }
    }
    console.log(counter);
  } else {
    return console.log(err);
  }
});
