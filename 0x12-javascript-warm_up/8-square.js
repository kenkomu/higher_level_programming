#!/usr/bin/node

/**
 * prints x times “C is fun”
 */

const size = process.argv[2];
let i; let j;

for (i = 0; i < size; i++) {
  for (j = 0; j < size; j++) {
    console.log('X');
  }
}
if (size === 0) {
  console.log('Missing size');
}
