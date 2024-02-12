#!/usr/bin/env python3

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getSmallestClockAngle(timeString, unit):
   # Write your code here

   if (h == 12):
       h = 0
   if (m == 60):
       m = 0
       h += 1
   if(h>12):
       h = h-12

   # Calculate the angles moved by
   # hour and minute hands with
   # reference to 12:00
   hour_angle = 0.5 * (h * 60 + m)
   minute_angle = 6 * m

   # Find the difference between two angles
   angle = abs(hour_angle - minute_angle)

   # Return the smaller angle of two
   # possible angles
   angle = min(360 - angle, angle)
   
   if unit == 'radians':
       angle = math.radians(angle)

   return angle

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
  output_1 = getSmallestClockAngle('03:00', 'radians')
  check(1.5708, output_1)

  output_2 = getSmallestClockAngle('09:30', 'degrees')
  check(105, output_2)

  # Add your own test cases here
  
