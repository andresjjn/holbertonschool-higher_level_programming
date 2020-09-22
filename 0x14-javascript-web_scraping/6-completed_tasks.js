#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const info = JSON.parse(body);
    for (const i in info) {
      if (info[i].completed === true) {
        if (!dict[info[i].userId]) {
          dict[info[i].userId] = 0;
        }
        dict[info[i].userId]++;
      }
    }
    console.log(dict);
  } else {
    return console.log(err);
  }
});
