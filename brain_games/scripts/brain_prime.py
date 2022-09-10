#!/usr/bin/env python3

from brain_games.games import is_prime
from brain_games.game_engine import run_game


def main():
    return run_game(is_prime)


if __name__ == '__main__':
    main()
