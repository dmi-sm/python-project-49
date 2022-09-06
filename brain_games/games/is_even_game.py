from random import randint
from brain_games.games.welcome_user import welcome_user
from brain_games.games.game_engine import game
from brain_games.games.Сonstant import WINSCORE


def right_answer(result):
    right_answer = 'yes' if result % 2 == 0 else 'no'
    return right_answer


def is_even():
    user_score = 0
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    while user_score < WINSCORE + 1:
        result = randint(1, 10)
        if game(result, right_answer(result), name, user_score) == True:
            user_score += 1
        else:
            break
