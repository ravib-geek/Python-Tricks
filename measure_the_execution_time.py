#!/usr/bin/python

# This code will help to measure time taken to execute code block in python

import time

class ExecutionTime:

    def __init__(self):
        self.start = None
        self.end = None

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print "Total time taken: %s" % self.duration()

    def duration(self):
        return str((self.end - self.start) * 1000) + ' milliseconds'

# EXAMPLE: to test the execution time for the function 'sum of range of numbers':
def sum1(n):
    final_sum = 0
    for x in range(n + 1):
        final_sum = final_sum + x
    return final_sum

with ExecutionTime() as ET:
    sum1(100)

