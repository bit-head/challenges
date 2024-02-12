#!/usr/bin/env python3

"""
You are given an array arr of size N. Find the number of all unique
pairs in the array that sum to a number k. The elements of the array
are distinct and are in sorted order.

Note: (a,b) and (b,a) are considered the same. Also, an element cannot
pair with itself, i.e., (a,a) is invalid.
"""

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

def countPairs(arr, k):
  # Write your code here
  print(k)
  res = []
  for n in arr:
      for d in arr:
          if sum((n,d)) == k and n != d:
              srt = sorted((n,d))
              if srt not in res:
                  res.append(srt)
  return len(res)








# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  output_1 = countPairs([1, 2, 3, 4, 5, 6, 7], 8)
  check(3, output_1)

  output_2 = countPairs([1, 2, 3, 4, 5, 6, 7], 98)
  check(0, output_2)

  # Add your own test cases here
