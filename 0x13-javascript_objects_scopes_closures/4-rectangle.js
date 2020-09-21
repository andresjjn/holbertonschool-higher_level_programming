#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (parseInt(w) && w > 0 && parseInt(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height = 2 * this.height;
    this.width = 2 * this.width;
  }
}
module.exports = Rectangle;
