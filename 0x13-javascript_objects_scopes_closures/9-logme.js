#!/usr/bin/node
let argumentnumber = 0;
exports.logMe = function (item) {
  console.log(argumentnumber + ': ' + item);
  argumentnumber++;
};
