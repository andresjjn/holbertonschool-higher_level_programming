#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const aCount = new Map([...new Set(list)].map(x => [x, list.filter(y => y === x).length]));
  return (aCount.get(searchElement));
};
