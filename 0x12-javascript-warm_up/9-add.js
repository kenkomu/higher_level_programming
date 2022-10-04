#!/usr/bin/node
function add (a, b) {
  let result;
  if (isNaN(parseInt(process.argv[2] || parseInt(process.argv[3])))) {
    console.log();
  } else {
    result = a + b;
    console.log(result);
  }
}
add(process.argv[2], process.argv[3]);
