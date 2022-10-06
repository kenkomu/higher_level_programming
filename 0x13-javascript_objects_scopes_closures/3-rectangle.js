#!/usr/bin/node

module.exports = class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      for (let column = 0; column < this.width; column++) {
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
};
