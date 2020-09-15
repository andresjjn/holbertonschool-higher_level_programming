#!/usr/bin/node
const a = parseInt(process.argv[2]);
function factorial (x) {
  if (x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}
if (!isNaN(a)) {
  console.log(factorial(a));
} else {
  console.log(1);
}
