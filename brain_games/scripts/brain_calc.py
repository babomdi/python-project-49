#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.calc import TASK, generate_calc


def main():
    run_game(TASK, generate_calc)


if __name__ == '__main__':
    main()
