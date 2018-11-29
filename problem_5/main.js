#!/usr/bin/env node

function cons(a, b) {
    return function pair(f) {
        return f(a, b);
    };
}

/////////////// ignore above this line ////////////////////
function car(cons) {
    return cons(function(a) {
        return a;
    });
}

function cdr(cons) {
    return cons(function(a, b) {
        return b;
    });
}

function main() {
    console.log('car: ' + car(cons(3, 4)));
    console.log('cdr: ' + cdr(cons(3, 4)));
}

main();
