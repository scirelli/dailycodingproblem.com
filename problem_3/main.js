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
const Node = require('./Node'),
    serialize = require('./serialize').cheap,
    deserialize = require('./deserialize').cheap;

function main() {
    let val = readLine();
    console.log(deserialize(serialize(new Node(val, new Node(), new Node()))));
}
