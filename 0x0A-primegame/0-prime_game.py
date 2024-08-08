#!/usr/bin/python3
"""Prime Game"""

def isWinner(x, nums):
    """Returns the name of the player that won the most rounds """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(nums):
        """Returns the next prime number in the list"""
        for num in nums:
            if is_prime(num):
                return num
        return None

    def play_round(nums):
        """Plays a round of the game"""
        while True:
            prime = get_next_prime(nums)
            if prime is None:
                return False  # No prime left, the other player wins
            nums = [n for n in nums if n % prime != 0]

    maria_wins = 0
    ben_wins = 0

    for _ in range(x):
        if play_round(nums):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # Cannot determine a winner