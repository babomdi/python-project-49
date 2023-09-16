from brain_games.engine import run_game
from random import randint


def generate_even():

    MIN_VALUE, MAX_VALUE = 0, 100
    num = randint(MIN_VALUE, MAX_VALUE)

    if num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return correct_answer, num


def run_even():

    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions_list = []
    correct_answers_list = []
    ROUNDS = 3

    for i in range(ROUNDS):
        correct_answer, num = generate_even()
        questions_list.append(num)
        correct_answers_list.append(correct_answer)

    run_game(task, questions_list, correct_answers_list)
