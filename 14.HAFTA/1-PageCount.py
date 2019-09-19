#!/bin/python3

import os
import sys


#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n - p < p:
        return (n - p) // 2
    else:
        return p // 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
