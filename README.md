# staircase
hackerrank staircase progam solving
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    a=n-1
    for i in range(1,n+1):
        for j in range(a,0,-1):
            print(" ",end="")
        for j in range(1,i+1):
            print("#",end="")
        a-=1
        print()

if __name__ == '__main__':
    n = int(input())

    staircase(n)
