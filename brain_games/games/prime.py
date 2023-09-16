from brain_games.engine import run_game
from random import randint
from math import sqrt


def generate_prime():

    MIN_VALUE, MAX_VALUE = 2, 100
    num = randint(MIN_VALUE, MAX_VALUE)

    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            correct_answer = 'no'
            return correct_answer, num
        else:
            correct_answer = 'yes'

    return correct_answer, num


def run_prime():

    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions_list = []
    correct_answers_list = []
    ROUNDS = 3

    for i in range(ROUNDS):
        correct_answer, num = generate_prime()
        questions_list.append(num)
        correct_answers_list.append(correct_answer)

    run_game(task, questions_list, correct_answers_list)
