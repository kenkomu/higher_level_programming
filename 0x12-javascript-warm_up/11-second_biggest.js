#!/usr/bin/node
let biggest = 0;
let secondBiggest = 0;
for (let index = 2; index < process.argv.length; index++) {
  const number = parseInt(process.argv[index]);

  if (biggest < number) {
    secondBiggest = biggest;
    biggest = number;
  } else if (secondBiggest < number) {
    secondBiggest = number;
  }
}
console.log(secondBiggest);
