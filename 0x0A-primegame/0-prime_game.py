#!/usr/bin/python3
'''
0. Prime Game
'''


def generate_primes(n):
    '''
    function to generate prime numbers up to a given limit.
    '''
    primes = []
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes


def is_prime(num):
    '''
    function to determine if a number is prime.
    '''
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def game_winner(primes, n):
    '''
    Simulate the game for a given n
    Returns the winner of the game
    '''
    maria_wins = False
    for i in range(len(primes)):
        if primes[i] > n:
            break
        n -= (n // primes[i]) + 1
        maria_wins = not maria_wins
    return "Maria" if maria_wins else "Ben"


def isWinner(x, nums):
    '''
    Implement the game logic using the generated primes.
    Simulate each round of the game, considering Maria always plays optimally.
    Count the number of wins for Maria and Ben.
    Determine the player with the most wins.
    '''
    most_wins = 0
    winner = None

    primes = generate_primes(10000)

    for n in nums:
        game_result = game_winner(primes, n)
        if game_result == "Maria":
            most_wins += 1
        elif game_result == "Ben":
            most_wins -= 1

    if most_wins > 0:
        winner = "Maria"
    elif most_wins < 0:
        winner = "Ben"

    return winner
