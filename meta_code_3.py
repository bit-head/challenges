#!/usr/bin/env python3

"""
Given an array arr[] of N non-negative integers
representing the height of blocks lined up directly
next to each other, if the width and depth of each
block is 1, compute how much water can be trapped
between the blocks during the rainy season.

Note: Water is trapped only on top of blocks when there
are boundaries to both the right and left of the blocks.

Signature

int getTrappedRainWater(int[] arr)

Input

Array arr of N integers (Ai)
3 <= N <= 107
0 <= Ai <= 108
"""

# Add any extra import statements you may need here


# Add any helper functions you may need here


def getTrappedRainWater(arr):
  # Write your code here
  # initialize variables
  # to set baseline
  n = len(arr)
  result = 0 
  left = 0
  right = n - 1
  max_left = 0
  max_right = 0

  # Loop until the two pointers meet
  while left <= right: 
      # If the left block is smaller than the right block
      if arr[left] < arr[right]:
          # If the left block is higher than the previous maximum
          if arr[left] > max_left:
              # Update the maximum height of the left block
              max_left = arr[left]
          else:
              # Add the difference between the maximum height and the current height to the result
              result += max_left - arr[left]
          # Move the left pointer to the right
          left += 1
      # If the right block is smaller than or equal to the left block
      else:
          # If the right block is higher than the previous maximum
          if arr[right] > max_right:
              # Update the maximum height of the right block
              max_right = arr[right]
          else:
              # Add the difference between the maximum height and the current height to the result
              result += max_right - arr[right]
          # Move the right pointer to the left
          right -= 1

  # Return the final result
  return result
  
  
  
  
  
  
  
   
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
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', expected, sep='', end='')
    print(' Your output: ', output, end='')
    print()
  test_case_number += 1

if __name__ == "__main__":
  outputOne = getTrappedRainWater([7,4,0,9]);
  check(10, outputOne);
  outputTwo = getTrappedRainWater([6,9,9]);
  check(0, outputTwo)
  # Add your own test cases here
  
