#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    v = 0
    m =0
    d=0
    for i in s:
        if i == 'U':
            d =d+1
        else:
            d= d-1
        if d==0 and i == 'U':
            v = v+1
    return v


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
