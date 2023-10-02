#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.progression import TASK, generate_progression


def main():
    run_game(TASK, generate_progression)


if __name__ == '__main__':
    main()
