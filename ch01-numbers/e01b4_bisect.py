#!/usr/bin/env python3
"""Solution to chapter 1, exercise 1, beyond 1: Guessing game, use bisect"""
import random
import click
from typing import List
import bisect
import math

@click.command()
@click.option('--max_number', type=int, default=100)
def guessing_game(max_number: int) -> None:
    """Generate a random integer from 1 to {max_number}.

    Ask the user repeatedly to guess the number.
    Until they guess correctly, tell them to guess higher or lower.
    If they take more than three times to guess, the program
    tells them that they're out of guesses.
    """
    answer = random.randint(0, max_number)
    remaining_guesses = math.ceil(math.log2(max_number))
    print(f'You have {remaining_guesses} guesses to guess the number between 0 and {max_number}')

    while remaining_guesses >= 0:
        remaining_guesses -= 1
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')

    else:
        print(f'The answer was {answer}')
        print('Your three chances are up!')

if __name__ == '__main__':
    guessing_game()
