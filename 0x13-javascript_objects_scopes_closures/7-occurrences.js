#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(function (element) {
    if (element === searchElement) {
      count++;
    }
  });
  return count;
};
