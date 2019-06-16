#!/usr/bin/env node
process.stdin.resume();
process.stdin.setEncoding('ascii');

var input_stdin = '';
var input_stdin_array = '';
var input_currentline = 0;

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split('\n');
    main();
});

function readLine() {
    return input_stdin_array[input_currentline++];
}

/////////////// ignore above this line ////////////////////
const listFewestPalindromes = require('./listFewestPalindromes');

function listFewestPalindromes(arr) {
    for(let i=arr.length-1; i>=0; i--) {
    }
}

// od -vAd -N40 -tu1 < /dev/urandom | cut -c11- | tr -s [:space:] " " | tee input2.txt
function main() {
    var arr = readLine().split('');
    
    console.log(listFewestPalindromes(arr));
}
