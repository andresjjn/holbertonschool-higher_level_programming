#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  if (list !== undefined && searchElement !== undefined) {
    const aCount = new Map([...new Set(list)].map(x => [x, list.filter(y => y === x).length]));
    const lists = [aCount.get(searchElement)];
    return (lists);
  }
  return (undefined);
};
