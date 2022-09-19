from math import gcd
from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_operand = randint(1, 10)
    second_operand = randint(1, 10)
    task = f'{first_operand} {second_operand}'
    answer = str(gcd(first_operand, second_operand))
    return (task, answer)
