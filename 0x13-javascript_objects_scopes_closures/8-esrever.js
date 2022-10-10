#!/usr/bin/node
exports.esrever = function (list) {
  const arr1 = [];
  while (list.length) {
    arr1.push(list.pop());
  }
  return arr1;
};
