#!/usr/bin/env node
/*
Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers 
between 0 and 255. Zero-prefixed numbers, such as 01 and 065, are not allowed, 
except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
 */
/*
    A B C D
    3+3+3+3  Max length = 12
    1+1+1+1  Min length = 4

    xxx.xxx.xxx.xxx  Length = 12 -> 1 combinations

    xxx.xxx.xxx.xx   Length = 11 -> 4 combinations

    xxx.xxx.xxx.x    Length = 10 -> 4 + 5 = 9 combinations
    xxx.xxx.xx.xx

    xxx.xxx.xx.x    Length = 9 -> 4 + 4
    xxx.xxx.x.xx
    xxx.x.xxx.xx
    x.xxx.xxx.xx
 */

function validIP(aQuads) {
    return aQuads.reduce((a,v)=>{
        return a && v.length <= 3 && parseInt(v) <= 255 && (v.length > 1 ? v[0] != '0' : true);
    }, true);
}

function generateIPs(str) {
    let ips = [];
    for(let Ai=1; Ai<=3; Ai++) {
        for(let Bi=1; Bi<=3; Bi++) {
            for(let Ci=1,ip=null; Ci<=3; Ci++) {
                //          012 345 678 9AB
                //          xxx xxx xxx xxx
                //
                //                  0           1                         2                                 3
                //                  x           x                         x                                 xxx xxx xxx
                //
                //                  0           1                         2 4)                              4
                //                  x           x                         x x                               xx xxx xxx
                ip = [str.substring(0, Ai), str.substring(Ai, Ai+Bi), str.substring(Ai+Bi, Ai+Bi+Ci), str.substring(Ai+Bi+Ci)];
                if(validIP(ip)) {
                    ips.push(ip.join('.'));
                }
            }
        }
    }
    return ips;
}

function testRunner() {
    const tests = [
        {
            str: '2542540123',
            expected: ['254.25.40.123', '254.254.0.123']
        },
        {
            str: '1111',
            expected: ['1.1.1.1']
        },
        {
            str: '255255255255',
            expected: ['255.255.255.255']
        },
        {
            str: '0255255255',
            expected: ['0.255.255.255']
        },
        {
            str: '0000',
            expected: ['0.0.0.0']
        },
        {
            str: '998998998998',
            expected: []
        }
    ];

    tests.forEach(test=> {
        let actual = generateIPs(test.str),
            expected = test.expected.reduce((a,v)=>{
                a[v] = true;
                return a;
            }, {});

        if(actual.length === 0 && test.expected.length === 0){
            process.stdout.write('P');
        }else if(actual.reduce((a, v)=> {
            return a && expected[v];
        }, true)) {
            process.stdout.write('P');
        }else{
            process.stdout.write('F');
            console.debug('Actual', actual, 'Expected', expected);
        }
    });
    process.stdout.write('\n');
}

function main() {
    testRunner();
}

main();
