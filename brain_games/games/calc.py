from operator import add, mul, sub
from random import randint, choice

GAME_RULE = 'What is the result of the expression?'
OPERATORS = {
        '+': add,
        '-': sub,
        '*': mul,
    }


def calc(operator, first_operand, second_operand):
    return OPERATORS[operator](first_operand, second_operand)


def game():
    operator = choice(list(OPERATORS.keys()))
    first_operand = randint(1, 10)
    second_operand = randint(1, 10)
    task = f'{first_operand} {operator} {second_operand}'
    answer = str(calc(operator, first_operand, second_operand))
    return (task, answer)
