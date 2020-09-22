#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
if (!url) {
  process.exit();
}
request(url, (err, res) => {
  if (err) return console.log(err);
  console.log(`code: ${res.statusCode}`);
});
