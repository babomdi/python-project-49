#!/usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.prime import TASK, generate_prime


def main():
    run_game(TASK, generate_prime)


if __name__ == '__main__':
    main()
