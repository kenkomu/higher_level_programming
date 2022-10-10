#!/usr/bin/node
const { list } = require('./100-map');
const map1 = list.map((Element, index) => Element * index);

console.log(list);
console.log(map1);
