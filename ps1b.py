###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise
import math
#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight=99, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here


    """
    GREEDY IMPLEMENTATION
    sorted_eggs = sorted(egg_weights, reverse = True)


    limit = target_weight
    remainder = limit
    transported_eggs = {}

    current_eggs = 0

    for egg in sorted_eggs:
        whole_eggs = math.floor(remainder/egg)
        transported_eggs[egg] = whole_eggs
        print(whole_eggs)
        remainder = remainder - (whole_eggs * egg)
        print(remainder)
    print(transported_eggs)
    """

    """"
    To do this with dynamic programming we want to pick an egg at weight n
    and then pick another egg, with all weights still available
    This is opposite of a greedy algorithm that goes through all of the biggest and then onward
    To resolve this we need to memoise the different weights and then take 
    the best one for the remaining number, i.e. biggest
    """
    """
    sorted_eggs = sorted(egg_weights, reverse=True)

    memo = {}
    for n in sorted_eggs:
        memo[n] = 0
    remainder = target_weight
    transport_eggs = {}
    multiplier = {}


    while remainder > 0:

        for n in memo:
            #print(remainder)
            multiplier[n] = math.floor((remainder/n))
        print(f"multiplier values: {multiplier}")
        possible_options = {key: value for key, value in multiplier.items() if value > 0}

        optimum_option = min(possible_options, key=possible_options.get)
        eggs_to_add = possible_options[optimum_option]

        memo[optimum_option] = memo[optimum_option] + eggs_to_add
        remainder = remainder - (eggs_to_add * optimum_option)
        multiplier.clear()

    print(memo)"""
    memo = {}
    sorted_weights = sorted(egg_weights, reverse=True)


    """
    For each instance of i 
    WE want to check:
        Is the number an input
            Is the number divisible by a number we have memoised
                If you subtract the memoised number from the number, is that divisible by a memoised number?
                
    """
    """
    for i in range(0,100):
        memo[i] = []
        current_list =[]
        for weight in sorted_weights:
            if weight == i:
                current_list.append(weight)
                memo[i] = current_list
            elif i % weight == 0 and weight != 1 and i > 0 and memo[i] == []:
                print("Divisible!")
                print(f"i = {i} and weight = {weight}")
                recursion = i - weight
                for block in memo:
                    if block > weight and block % weight == 0 and memo[i] ==[]:
                        print(f"Weight: {weight} and recursion = {recursion}")
                        current_list.append(memo[weight])
                        current_list.append(memo[recursion])
                        memo[i] = current_list
                print("why...?")
                if memo[i] == []:
                    multiplier = int(i/weight)
                    for n in range(0,multiplier):
                        current_list.append(weight)
                    memo[i] = current_list

            elif len(memo[i]) < 1 and i > 0 and i - weight == (i-1) and memo[i] == []:
                current_list.append([weight])
                current_list.append(memo[i-1])
                memo[i] = current_list
            else:
                pass
    for m in memo.items():
        print(m)
    """
    """
    # Step 1: Initialize DP array
    dp = [float('inf')] * (target_weight + 1)
    dp[0] = 0  # Base case: 0 eggs needed for 0 weight

    # Step 2: Bottom-up dynamic programming solution
    for weight in range(1, target_weight + 1):
        for egg in egg_weights:
            if egg <= weight:
                print("Weight: ", weight)
                print(f"DP Weight: {dp[weight]}, dp weight - egg = {dp[weight-egg]}")
                dp[weight] = min(dp[weight], 1 + dp[weight - egg])
                print()
    print(dp)
    # Return the minimum number of eggs needed for the target weight
    return dp[target_weight]
    """

    target = target_weight
    eggs = sorted(egg_weights, reverse = True)
    memo = [None] * (target + 1)
    memo[0] = []  # Base case: 0 weight requires 0 eggs

    for i in range(1, target + 1):
        for egg in eggs:
            if egg <= i:
                # Check if we can form this weight by adding this egg to a combination that forms the remainder
                remainder = i - egg
                print(i)
                print("remainder ", remainder)
                if memo[remainder] is not None:
                    # If there's a valid combination for the remainder, use it and add the current egg
                    combination = memo[remainder] + [egg]
                    # Update memo[i] if it's either empty or if we found a better (shorter) combination
                    if memo[i] is None or len(combination) < len(memo[i]):
                        memo[i] = combination
    print(memo)












    pass

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    """print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()"""

    print(dp_make_weight(egg_weights))