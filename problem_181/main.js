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

// od -vAd -N400 -tc < /dev/urandom | cut -c11- | tr -s [:space:] " " | tr -cd '[:alpha:]' | tee input.txt
function main() {
    console.log(listFewestPalindromes(readLine()).join(', '));
}
