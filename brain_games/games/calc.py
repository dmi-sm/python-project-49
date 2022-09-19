from operator import add, mul, sub
from random import randint, choice

GAME_RULE = 'What is the result of the expression?'
OPERATORS = ('*', '+', '-')


def calculate_expression(operator, first_operand, second_operand):
    if operator == '*':
        return mul(first_operand, second_operand)
    if operator == '+':
        return add(first_operand, second_operand)
    if operator == '-':
        return sub(first_operand, second_operand)


def get_question_and_answer():
    operator = choice(OPERATORS)
    first_operand = randint(1, 10)
    second_operand = randint(1, 10)
    task = f'{first_operand} {operator} {second_operand}'
    answer = str(calculate_expression(operator, first_operand, second_operand))
    return (task, answer)
