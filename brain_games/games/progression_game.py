from random import randint
from brain_games.games.game_engine import game
from brain_games.games.welcome_user import welcome_user
from brain_games.games.Сonstant import WINSCORE


def right_answer(missing_number):
    right_answer = missing_number
    return right_answer


def progression():
    user_score = 0
    start_progression = 0
    step_progression = 0
    length_progression = 5
    progression = []
    result = []
    name = welcome_user()
    print('What number is missing in the progression?')
    while user_score < WINSCORE + 1:
        start_progression = randint(1, 10)
        step_progression = randint(1, 10)
        progression = [str(i) for i in range(start_progression,
                                             start_progression +
                                             length_progression *
                                             step_progression,
                                             step_progression)]
        missing_number_index = randint(0, length_progression - 1)
        missing_number = progression[missing_number_index]
        progression[missing_number_index] = '..'
        result = progression
        if game(result, right_answer(missing_number), name, user_score):
            user_score += 1
        else:
            break
