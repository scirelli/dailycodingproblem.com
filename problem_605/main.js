#!/usr/bin/env node
/*
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
*/
const {performance} = require('perf_hooks');

(()=>{
    const input = [
        [4, 3, 0, 1, 5],
        [1, 1],
        [4, 1, 4, 1, 4, 1, 4, 1, 5, 5],
        [4, 4, 4, 4, 5, 5],
        [2, 3, 1],
        [4, 4, 5, 6, 3],
        [5, 6],
        fill(0, 100001, 10000)
    ];

    let r, t, e;

    [determineHIndex, determineHIndex_fastest].forEach((f)=>{
        t = performance.now();
        r = input.map(f);
        e = performance.now();
        console.log(r.join('\n'), (e-t)/1000, 's');
    });

    //O(n^2)
    function determineHIndex(list) {
        let results = [];

        for(let i=0, h, cnt=0; i<list.length; i++) {
            h = list[i];
            cnt = 0;
            for(let j=0, c; j<list.length;  j++) {
                c = list[j];
                if(c>=h) cnt++;
            }
            if(cnt>=h) results.push(h);
        }

        if(!results.length) {
            return null;
        }

        return Math.max(...results);
    }

    function determineHIndex_fastest(input) {
        input = input.sort((a, b)=>a-b);

        let midIndex = Math.floor(input.length/2),
            rtn = null;

        //go up
        for(let i=midIndex, end=input.length; i >= 0; i--) {
            if(input[i] <= (end-i)) {
                rtn = input[i];
                break;
            }
        }

        return rtn;
    }

    function randRange(b, e) {
        return ~~(((e - b) * Math.random()) + b);
    }
    function fill(b, e, size) {
        let rtn = [];
        for(let i=0; i<size; i++) {
            rtn.push(randRange(b, e));
        }
        return rtn;
    }
})();
