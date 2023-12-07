#!/usr/bin/python3
''' checks for the winner of a game using prime numbers'''


def isWinner(x, nums):
    '''
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    '''
    def is_prime(num):
        '''check of num is prime'''
        for i in range(2, int(num**0.5) + 1):
            if not num % i:
                return False
        return True

    def calculate_primes(n, primes):
        '''calculates the number of primes that can be gotten in a prime
        number
        '''
        top_prime = primes[-1]
        if n > top_prime:
            for i in range(top_prime + 1, n + 1):
                if is_prime(i):
                    primes.append(i)
                else:
                    primes.append(0)

    def game_winner(n, primes):
        '''finds the game winner'''
        sum_options = sum((i != 0 and i <= n) for i in primes[:n + 1])
        return "Maria" if sum_options % 2 else "Ben"

    players_wins = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]

    for round in range(x):
        calculate_primes(nums[round], primes)
        winner = game_winner(nums[round], primes)

        if winner:
            players_wins[winner] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
