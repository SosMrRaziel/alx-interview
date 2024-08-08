#!/usr/bin/python3
"""Prime Game"""

def isWinner(x, nums):
    """ Initialize counters for Maria and Ben's wins """
    maria_wins = 0
    ben_wins = 0

    # Play each round of the game
    for n in nums:
        # Calculate the sum of prime numbers in the set
        prime_sum = sum([i for i in range(2, n + 1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))])

        # Determine the winner of the game
        if prime_sum % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Compare the wins and return the winner
    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
