#!/usr/bin/env node
/*
* Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
* If there are multiple smallest sets, return any of them.
*
* For example:
*   given the intervals
*   [0, 3], [2, 6], [3, 4], [6, 9]
*   one set of numbers that covers all these intervals is
*   {3, 6}
*/
process.stdin.resume();
process.stdin.setEncoding('ascii');

let input_stdin = '';
let input_stdin_array = '';

process.stdin.on('data', function (data) {
    input_stdin += data;
});

process.stdin.on('end', function () {
    input_stdin_array = input_stdin.split('\n').filter(Boolean);
    main(parseInput());
});

function parseInput() {
    return input_stdin_array.map(l=>l.split(',').map(Number));
}


function main(intervals) {
    let result = {leftOver: intervals},
        set = {};
    while(result.leftOver.length) {
        result = buildSet(result.leftOver);
        set[result.num] = true;
    }
    console.log(Object.keys(set));
}

//---------------------------------------------
// 0, 1, 2, 3
//       2, 3, 4, 5, 6
//          3, 4                         {3,6}
//                   6, 7, 8, 9
//---------------------------------------------
// 0, 1, 2, 3
//       2, 3, 4, 5, 6
//          3, 4                         {3,6}
//                   6, 7, 8, 9
// 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
//---------------------------------------------
// 0, 1, 2, 3
//       2, 3, 4, 5, 6
//          3, 4                         {3}
// 0, 1, 2, 3
//---------------------------------------------
// 0, 1, 2, 3
//    1, 2, 3, 4, 5, 6
//          3, 4                         {3}
// 0, 1, 2, 3
//---------------------------------------------
// 0, 1, 2, 3
// 0, 1, 2, 3
// 0, 1, 2, 3                            {0}
// 0, 1, 2, 3
//---------------------------------------------
// 0, 1, 2, 3
//       2, 3, 4, 5, 6
//          3, 4                         {3,7}
//                     7, 8, 9, 10
//---------------------------------------------
// 0, 1, 2, 3
//       2, 3, 4, 5, 6
//          3, 4                         {3,10}
//                     7, 8, 9, 10
//                           9, 10, 11
//---------------------------------------------
// 0, 1, 2, 3
//       2, 3, 4, 5, 6
//          3, 4                         {3,9}
//                     7, 8, 9, 10
//                           9, 10, 11
//                     7, 8, 9
function buildSet(intervals) {
    const START = 0,
        END = 1;

    let leftOver = [],
        set = intervals.reduce((a, interval)=> {
            for(let i=interval[START]; i<=interval[END]; i++) {
                if(a[i]) {
                    a[i]++;
                }
                else a[i] = 1;
            }
            return a;
        }, {});

    let maxNum = 0, r;
    for(let num in set) {
        if(set[num] > maxNum) {
            maxNum = set[num];
            r = num;
        }
    }
    r = parseInt(r);
    leftOver = intervals.filter(i=> {
        if(r >= i[START] && r <= i[END]) return false;
        return true;
    });

    return {num: r, leftOver: leftOver};
}
