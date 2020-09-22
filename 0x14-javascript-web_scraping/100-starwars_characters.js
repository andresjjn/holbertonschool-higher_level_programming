#!/usr/bin/node
const request = require('request');
const movie = process.argv[2];
if (!movie) {
  process.exit();
}
request(`https://swapi-api.hbtn.io/api/films/${movie}`, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const info = JSON.parse(body);
    for (const i in info.characters) {
      request(info.characters[i], (error, responses, bodys) => {
        if (!error && responses.statusCode === 200) {
          const char = JSON.parse(bodys);
          console.log(char.name);
        } else {
          return console.log(error);
        }
      });
    }
  } else {
    return console.log(err);
  }
});
