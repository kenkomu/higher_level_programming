#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  this.list = [5, 5, 5, 2, 2, 2, 2, 2, 9, 4];
  this.searchElement = {};

  for (const element of list) {
    if (searchElement[element]) {
      searchElement[element] += 1;
    } else {
      searchElement[element] = 1;
    }
  }
};
