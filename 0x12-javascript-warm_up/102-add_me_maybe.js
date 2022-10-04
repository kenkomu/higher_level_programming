#!/usr/bin/node
exports.callMeMoby = function (number, theFunction) {
  number++;
  theFunction(number);
};
