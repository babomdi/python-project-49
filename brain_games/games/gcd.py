from brain_games.engine import run_game
from random import randint
from math import gcd


def generate_gcd():

    MIN_VALUE, MAX_VALUE = 1, 100
    num1 = randint(MIN_VALUE, MAX_VALUE)
    num2 = randint(MIN_VALUE, MAX_VALUE)
    correct_answer = str(gcd(num1, num2))

    return correct_answer, num1, num2


def run_gcd():

    task = 'Find the greatest common divisor of given numbers.'
    questions_list = []
    correct_answers_list = []
    ROUNDS = 3

    for i in range(ROUNDS):
        correct_answer, num1, num2 = generate_gcd()
        questions_list.append(f'{num1} {num2}')
        correct_answers_list.append(correct_answer)

    run_game(task, questions_list, correct_answers_list)
