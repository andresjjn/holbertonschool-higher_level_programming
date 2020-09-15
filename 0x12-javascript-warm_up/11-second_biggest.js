#!/usr/bin/node
if (process.argv.length > 3) {
  let array = process.argv.slice(2);
  for (let index = 0; index < array.length; index++) {
    array[index] = parseInt(array[index], 10);
  }
  array = array.sort(function (a, b) {
    return a - b;
  });
  console.log(array[array.length - 2]);
} else {
  console.log(0);
}
