#!/usr/bin/node
const a = parseInt(process.argv[2]);
let b = 1;
if (!isNaN(a)) {
  for (let index = 1; index <= a; index++) {
    b = b * index;
  }
}
console.log(b);
