#!/usr/bin/node
const times = parseInt(process.argv[2]);
if (!isNaN(times) && process.argv.length >= 3) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}
