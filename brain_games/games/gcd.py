from math import gcd as find_gcd
from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def gcd(first_operand, second_operand):
    return str(find_gcd(first_operand, second_operand))


def game():
    first_operand = randint(1, 10)
    second_operand = randint(1, 10)
    task = f'{first_operand} {second_operand}'
    answer = gcd(first_operand, second_operand)
    return (task, answer)
