from math import gcd as find_gcd
from random import randint
from brain_games.games.game_engine import game
from brain_games.games.welcome_user import welcome_user
from brain_games.games.Сonstant import WINSCORE


def right_answer(result):
    first_operand = int(result.split()[0])
    second_operand = int(result.split()[1])
    right_answer = str(find_gcd(first_operand, second_operand))
    return right_answer


def gcd():
    user_score = 0
    first_operand = 0
    second_operand = 0
    result = 0
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    while user_score < WINSCORE + 1:
        first_operand = randint(1, 10)
        second_operand = randint(1, 10)
        result = f'{first_operand} {second_operand}'
        if game(result, right_answer(result), name, user_score):
            user_score += 1
        else:
            break
