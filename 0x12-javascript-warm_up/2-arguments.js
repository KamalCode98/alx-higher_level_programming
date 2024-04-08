#!/usr/bin/node

const args = process.argv;
let text;

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

console.log('text');
