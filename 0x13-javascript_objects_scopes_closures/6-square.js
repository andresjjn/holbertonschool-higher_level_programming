#!/usr/bin/node
const Squares = require('./5-square');
class Square extends Squares {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
