# problem 1
# careful for return

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    return sum(ar[:])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

bool(a[0] > b[0])