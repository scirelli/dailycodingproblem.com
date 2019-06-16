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
        {given: 'a', expected: ['a']},
        {given: 'ab', expected: ['a', 'b']},
        {given: 'abc', expected: ['a', 'b', 'c']},
        {given: 'aaa', expected: ['aaa']},
        {given: 'aaaaaabcba', expected: ['aaaaa', 'abcba']}
    ];

    tests.forEach((test, index)=> {
        let result;
        try{
            result = listFewestPalindromes(test.given);
            assert(result.equals(test.expected));
            console.log(result, test.expected);
            console.log(`${index+1} Passed`);
        }catch(e) {
            console.error(test.expected, ' did not equal ', result);
        }
    });
})();
