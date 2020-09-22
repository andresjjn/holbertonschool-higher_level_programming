#!/usr/bin/node
const file = require('fs');
const path = process.argv[2];
if (!path) {
  process.exit();
}
file.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
