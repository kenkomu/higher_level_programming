#!/usr/bin/node
const { dict } = require('101-data');
const newDict = {};
for (const [, value] of Object.entries(dict)) {
  const list = [];

  for (const [key, dictValue] of Object.entries(dict)) {
    if (dictValue === value) {
      list.push(key);
    }
  }

  newDict[value] = list;
}

console.log(newDict);
