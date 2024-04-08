#!/usr/bin/node

const args = process.argv;
let message;

if (args.length <= 2) {
  message = 'No argument';
} else if (args.length === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

console.log(message);
