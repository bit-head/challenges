#!/usr/bin/env python3

my_dict = {}

my_dict['small'] = 125
my_dict['medium'] = 50
my_dict['large'] = 500

stalls = input("Which size stall would you like, small, medium, or large: ")
if stalls.lower() in my_dict.keys():
    print('You picked %s with value: %d' % (stalls, my_dict[stalls]))
else:
    print('No value found for: %s' % (stalls) )
