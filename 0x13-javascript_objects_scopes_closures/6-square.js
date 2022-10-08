#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let row = 0; row < this.size; row++) {
      for (let column = 0; column < this.size; column++) {
        process.stdout.write('c');
        if (c === undefined);
        process.stdout.write('X');
      }
      process.stdout.write('\n');
    }
  }
};
