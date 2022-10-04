#!/usr/bin/node

/**
 * prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
 */
const message = Array['C is fun' + 'Python is cool' + 'JavaScript is amazing'];

message.foreach(element => (console.log(element)));
