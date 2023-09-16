from brain_games.engine import run_game
from random import randint


def generate_progression():

    progression = []
    MIN_VALUE, MAX_VALUE = 1, 10
    num = randint(MIN_VALUE, MAX_VALUE)
    progression.append(num)
    MIN_DIFFERENCE, MAX_DIFFERENCE = 1, 20
    difference = randint(MIN_DIFFERENCE, MAX_DIFFERENCE)

    for i in range(9):
        next_num = num + difference
        progression.append(next_num)
        num = next_num

    HIDDEN_INDEX_MIN, HIDDEN_INDEX_MAX = 0, 9
    hidden_index = randint(HIDDEN_INDEX_MIN, HIDDEN_INDEX_MAX)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'

    return correct_answer, progression


def run_progression():

    task = 'What number is missing in the progression?'
    questions_list = []
    correct_answers_list = []
    ROUNDS = 3

    for i in range(ROUNDS):
        correct_answer, progression = generate_progression()
        correct_answers_list.append(correct_answer)
        questions_list.append(' '.join(map(str, progression)))

    run_game(task, questions_list, correct_answers_list)
