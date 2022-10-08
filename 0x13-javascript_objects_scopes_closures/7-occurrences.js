#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  this.list = [5, 5, 5, 2, 2, 2, 2, 2, 9, 4];
  this.searchElement = {};

  for (const num of list) {
    searchElement[num] = searchElement[num] ? searchElement[num] + 1 : 1;
  }
};
