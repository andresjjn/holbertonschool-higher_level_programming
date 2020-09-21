#!/usr/bin/node
exports.esrever = function (list) {
  const lists = [];
  for (let index = list.length - 1; index >= 0 ; index--) {
    lists.push(list[index]);
  }
  return (lists);
};
