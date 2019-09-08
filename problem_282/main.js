#!/usr/bin/env node
/*
This problem was asked by Netflix.

Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a^2 + b^ 2= c^2.
*/
Math.randRange = function randRange(start, end) {
    return ~~(this.random() * (end - start) + start);
};

Array.prototype.swap = function swap(from, to) {
    let tmp = this[to];
    this[to] = this[from];
    this[from] = tmp;
    return this;
};

Array.prototype.shuffle = function shuffle() {
    for(let i=0; i<this.length; i++) {
        this.swap(i, Math.randRange(0, this.length));
    }
    return this;
};

//n^2
function hasPythagoreanTriplet(arr) {
    let squares = arr.reduce((accum, val)=>{ accum.push(val*val); return accum; }, []),
        squareMap = squares.reduce((accum, val)=>{ accum[val] = true; return accum;}, {});

    for(let i=0, a; i<squares.length; i++) {
        a = squares[i];
        for(let j=i+1, b; j<squares.length-1; j++) {
            b = squares[j];
            if(squareMap[a+b]) {
                return true;
            }
        }
    }

    return false;
}

//n^2 - n
function hasPythagoreanTriplet2(arr) {
    let squares = arr.reduce((accum, val)=>{ accum.push(val*val); return accum; }, []),
        sum = 0;

    for(let i=0, l=squares.length; i<l; i++) {
        sum = squares.shift();
        if(findSum(squares, sum)) {
            return true;
        }
        squares.push(sum);
    }

    return false;
    function findSum(arr, sum) {
        let fMap = {};

        for(let i=0, val, diff; i<arr.length; i++) {
            val = arr[i];
            diff = sum - val;
            if(fMap[diff]) {
                return true;
            }
            fMap[val] = true;
        }
        return false;
    }
}
//triplet = [3, 4, 5],
let size = 1000000, arr = Array(size).map(()=>Math.randRange(0, size)).shuffle(),
    never = Array(size).fill(1);

[arr, never].forEach((arr)=> {
    let start, end1, end2;

    start = process.hrtime();
    hasPythagoreanTriplet(arr);
    end1 = process.hrtime(start);
    console.log(hrToNano(end1)/1e9 + 's');

    start = process.hrtime();
    hasPythagoreanTriplet2(arr);
    end2 = process.hrtime(start);
    console.log(hrToNano(end2)/1e9 + 's');

});

function hrToNano(hrt) {
    return hrt[0] * 1e9 + hrt[1];
}
