#!/usr/bin/env node
const listFewestPalindromes = require('./listFewestPalindromes');
const assert = require('assert');

if(!Array.prototype.includesAll) {
    Array.prototype.includesAll = function(arr) {
        for(let i=0, l=arr.length; i<l; i++) {
            if(!this.includes(arr[i])) {
                return false;
            }
        }
        return true;
    };
}

if(!Array.prototype.equals) {
    Array.prototype.equals = function(arr) {
        if(this.length !== arr.length) return false;
        for(let i=0, l=arr.length; i<l; i++) {
            if(!this.includes(arr[i])) {
                return false;
            }
        }
        return true;
    };
}

(function test() {
    const tests = [
        {given: 'aabbaa',              expected: ['aabbaa']},
        {given: 'a',                   expected: ['a']},
        {given: 'ab',                  expected: ['a', 'b']},
        {given: 'abc',                 expected: ['a', 'b', 'c']},
        {given: 'aaa',                 expected: ['aaa']},
        {given: 'aaaaaabcba',          expected: ['aaaaa', 'abcba']},
        {given: 'racecarannakayak',    expected: ['racecar', 'anna', 'kayak']},
        {given: 'Kayakdcrapjanna1.3&', expected: [ 'Kayak', 'd', 'c', 'r', 'a', 'p', 'j', 'anna', '1', '.', '3', '&' ]}
    ];

    tests.forEach((test, index)=> {
        let result;
        try{
            result = listFewestPalindromes(test.given);
            assert(result.equals(test.expected));
            console.log(`Test ${index+1} '${test.given}' Result [${result}], Expected [${test.expected}] --> Passed.`);
        }catch(e) {
            console.error(test.expected, ' did not equal ', result);
        }
    });
})();
