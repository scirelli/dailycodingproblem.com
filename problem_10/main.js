#!/usr/bin/env node

var jobs = [
    {
        func: function() {
            for(var i=0; i<1000000; i++) console.log(i);
        },
        time: 1000
    },
    {
        func: function() {
            console.log('Job running');
        },
        time: 1001
    }
];

jobs.forEach((job)=> {
    setTimeout(job.func, job.time);
});
