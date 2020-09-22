#!/usr/bin/node
const lists = require('./100-data').list;
const mapping = lists.map((current, index) => { return current * index; });
console.log(lists);
console.log(mapping);
