from brain_games.engine import run_game
from random import randint, choice


def generate_calc():

    operators = ['+', '-', '*']
    MIN_VALUE, MAX_VALUE = 0, 100
    num1 = randint(MIN_VALUE, MAX_VALUE)
    num2 = randint(MIN_VALUE, MAX_VALUE)
    random_operator = choice(operators)

    if random_operator == '+':
        correct_answer = num1 + num2
    elif random_operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return correct_answer, num1, num2, random_operator


def run_calc():

    task = 'What is the result of the expression?'
    questions_list = []
    correct_answers_list = []
    ROUNDS = 3

    for i in range(ROUNDS):
        correct_answer, num1, num2, operator = generate_calc()
        questions_list.append(f'{num1} {operator} {num2}')
        correct_answers_list.append(str(correct_answer))

    run_game(task, questions_list, correct_answers_list)
