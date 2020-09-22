#!/usr/bin/node
const file = require('fs');
const path = process.argv[2];
const message = process.argv[3];
file.appendFile(path, message, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
