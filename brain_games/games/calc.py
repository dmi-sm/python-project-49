from operator import add, mul, sub
from random import randint, choice

GAME_RULE = 'What is the result of the expression?'
OPERATIONS = (
    ('+', add),
    ('-', sub),
    ('*', mul),
)


def get_question_and_answer():
    operator_name, operator_method = choice(OPERATIONS)
    first_operand = randint(0, 10)
    second_operand = randint(0, 10)
    task = f'{first_operand} {operator_name} {second_operand}'
    answer = str(operator_method(first_operand, second_operand))
    return (task, answer)
