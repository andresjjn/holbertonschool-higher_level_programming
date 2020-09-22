#!/usr/bin/node
const dic = require('./101-data').dict;
const dic2 = {};
for (const [key, value] of Object.entries(dic)) {
  if (!dic2[value]) {
    dic2[value] = [];
  }
  dic2[value].push(key);
}
console.log(dic2);
