#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let row = 0; row < this.height; row++) {
        for (let column = 0; column < this.width; column++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
};
