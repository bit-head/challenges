#!/usr/bin/env python3

import itertools

digits = "6223"

def letterCombinations(digits: str) -> list[str]:
    fl_lst = []
    results = {}
    combinations = []
    
    if digits:
        phone_digits = {}
        phone_digits[2] = ["a", "b", "c"]
        phone_digits[3] = ["d", "e", "f"]
        phone_digits[4] = ["g", "h", "i"]
        phone_digits[5] = ["j", "k", "l"]
        phone_digits[6] = ["m", "n", "o"]
        phone_digits[7] = ["p", "q", "r", "s"]
        phone_digits[8] = ["t", "u", "v"]
        phone_digits[9] = ["w", "x", "y", "z"]
    
        i = 0
    
        for d in digits:
           results[i] = phone_digits[int(d)]
           i += 1
        combinations = itertools.product(*results.values())
        combinations = ["".join(pair) for pair in combinations]
        fl_lst = list(combinations)

    return fl_lst


print(letterCombinations(digits))
