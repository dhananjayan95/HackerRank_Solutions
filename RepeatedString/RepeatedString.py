#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count1 = s.count('a')
    if (n%len(s) == 0):
        return int(count1*(n/len(s)))
    else:
        count1 = count1*math.floor(n/len(s))
        count1 = count1 + s[:n%len(s)].count('a')
        return int(count1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
