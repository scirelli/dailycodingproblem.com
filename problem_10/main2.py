#!/usr/bin/env python3
import threading


class Job():
    def __init__(self, ms_delay, func):
        self.ms_delay = ms_delay
        self.func = func


jobsList = [
    Job(1000, lambda: print('running')),
    Job(10, lambda: print('shorter running'))
]


def runner(jobs):
    for job in jobs:
        threading.Timer(job.ms_delay / 1000, job.func).start()


if __name__ == '__main__':
    runner(jobsList)
