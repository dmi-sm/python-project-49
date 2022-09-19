from random import randint

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(task):
    for i in range(2, (task // 2) + 1):
        if task % i == 0:
            return False
    return True


def get_question_and_answer():
    task = randint(2, 10)
    answer = 'yes' if is_prime(task) is True else 'no'
    return (task, answer)
