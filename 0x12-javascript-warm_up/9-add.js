#!/usr/bin/node

/**
 * Add two numbers
 *
 * @param {*} a first number
 * @param {*} b second number
 *
 * @returns result of addition of two parameters
 */
function add (a, b) {
  return (a + b);
}
/**
 * prints the addition of 2 integers
 */
console.log(add(parseInt(process.argv[2]), (parseInt(process.argv[3]))));
