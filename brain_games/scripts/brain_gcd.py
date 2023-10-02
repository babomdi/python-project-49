#!usr/bin/env python3
from brain_games.engine import run_game
from brain_games.games.gcd import TASK, generate_gcd


def main():
    run_game(TASK, generate_gcd)


if __name__ == '__main__':
    main()
