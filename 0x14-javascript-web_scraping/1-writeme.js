#!/usr/bin/node
const file = require('fs');
const path = process.argv[2];
const message = process.argv[3];
if (!path || !message) {
  process.exit();
}
file.appendFile(path, message, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
