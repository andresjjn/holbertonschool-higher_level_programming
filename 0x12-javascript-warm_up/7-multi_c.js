#!/usr/bin/node
const xC = 'C is fun';
const times = parseInt(process.argv[2]);
if (!isNaN(times) && process.argv.length >= 3) {
  for (let index = 0; index < process.argv[2]; index++) {
    console.log(xC);
  }
} else {
  console.log('Missing number of occurrences');
}
