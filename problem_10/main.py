#!/usr/bin/env python3
import sched
import time
import threading

scheduler = sched.scheduler(time.perf_counter, time.sleep)

def print_event(name, start_time):
    now = time.time()
    elapsed = int(now - start_time)
    print('EVENT: {} elapsed={} name={}'.format(time.ctime(now), elapsed, name))


start = time.time()
print('START:', time.ctime(start))
scheduler.enter(2, 1, print_event, ('first', start))
scheduler.enter(3, 1, print_event, ('second', start))

scheduler.run()
