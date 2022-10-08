#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (width, height, size) {
    super(width, height);
    this.size = size;
  }
};
