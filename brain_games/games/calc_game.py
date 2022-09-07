from operator import add, mul, sub
from random import randint, choice
from brain_games.games.game_engine import game
from brain_games.games.welcome_user import welcome_user
from brain_games.games.Сonstant import OPERANDS, WINSCORE


def right_answer(result):
    operand = result.split()[1]
    first_operand = int(result.split()[0])
    second_operand = int(result.split()[2])
    if operand == '+':
        right_answer = str(add(first_operand, second_operand))
    if operand == '-':
        right_answer = str(sub(first_operand, second_operand))
    if operand == '*':
        right_answer = str(mul(first_operand, second_operand))
    return right_answer


def calc():
    user_score = 0
    operand = ''
    first_operand = 0
    second_operand = 0
    result = 0
    name = welcome_user()
    print('What is the result of the expression?')
    while user_score < WINSCORE + 1:
        operand = choice(OPERANDS)
        first_operand = randint(1, 10)
        second_operand = randint(1, 10)
        result = f'{first_operand} {operand} {second_operand}'
        if game(result, right_answer(result), name, user_score):
            user_score += 1
        else:
            break
