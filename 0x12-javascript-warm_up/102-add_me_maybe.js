#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  number += 1;
  theFunction();
}
exports.addMeMaybe = addMeMaybe;
