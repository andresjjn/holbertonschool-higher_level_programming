#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add (a, b) {
  let c = 0;
  c = a + b;
  return c;
}
if (a !== undefined && b !== undefined) {
  console.log(add(a, b));
}
