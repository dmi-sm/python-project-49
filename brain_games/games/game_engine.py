import prompt
from brain_games.games.Сonstant import (CONGRATULATIONS, CORRECT, QUESTION,
                                        TRY_AGAIN, WINSCORE, WRONG_ANSWER)


def game(result, right_answer, name, user_score):
    if user_score == WINSCORE:
        print(f'{CONGRATULATIONS}{name}!')
        return False
    else:
        print(f'{QUESTION}: {result}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print(f'{CORRECT}')
            return True
        else:
            print(f'"{user_answer}"{WRONG_ANSWER}"{right_answer}"')
            print(f'{TRY_AGAIN}{name}!')
            return False
