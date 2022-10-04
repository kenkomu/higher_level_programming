#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
exports.incr = function (value) {
  return value++;
};
