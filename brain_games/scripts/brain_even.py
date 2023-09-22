#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.even import TASK, get_questions_and_answers


def main():
    run_game(TASK, get_questions_and_answers)


if __name__ == '__main__':
    main()
