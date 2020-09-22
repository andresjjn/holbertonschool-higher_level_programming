#!/usr/bin/node
const list = require('./100-main').list;
const mapping = list.map((current, index) => current * index);
console.log(list);
console.log(mapping);
