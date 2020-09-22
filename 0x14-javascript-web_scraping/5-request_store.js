#!/usr/bin/node
const request = require('request');
const file = require('fs');
const url = process.argv[2];
const path = process.argv[3];
request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    file.appendFile(path, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    return console.log(err);
  }
});
