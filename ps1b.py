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