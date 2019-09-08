#!/usr/bin/env node
/*
This problem was asked by Google.

A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
*/
//Reference https://rosettacode.org/wiki/Hamming_numbers#JavaScript

function *hamming() {
    let queues = {2: [], 3: [], 5: []},
        base,
        next_ham = 1,
        a;

    while (true) {
        yield next_ham;
        for(base in queues) {
            queues[base].push(next_ham * base);
        }

        a = [];
        for(let queue of Object.values(queues)) {
            a.push(queue[0]);
        }
        next_ham = a.reduce(function(min, val) {
            return Math.min(min, val);
        });

        for(base in queues) {
            if(queues[base][0] === next_ham) {
                queues[base].shift();
            }
        }
    }
}

var ham = hamming();
var first20=[], i=1;

for (; i <= 20; i++)
    first20.push(ham.next().value);
console.log(first20.join(', '));
console.log('...');
for (; i <= 1690; i++)
    ham.next();
console.log(i + ' => ' + ham.next().value);
