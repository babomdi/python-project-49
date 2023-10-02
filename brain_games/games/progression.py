from random import randint


MIN_VALUE, MAX_VALUE = 1, 10
MIN_DIFFERENCE, MAX_DIFFERENCE = 1, 20
HIDDEN_INDEX_MIN, HIDDEN_INDEX_MAX = 0, 9
PROGRESSION_LENGTH = 10
TASK = 'What number is missing in the progression?'


def get_progression(num, difference):

    progression = []
    progression.append(num)

    for i in range(PROGRESSION_LENGTH - 1):
        next_num = num + difference
        progression.append(next_num)
        num = next_num

    return progression


def generate_progression():

    num = randint(MIN_VALUE, MAX_VALUE)
    difference = randint(MIN_DIFFERENCE, MAX_DIFFERENCE)

    progression = get_progression(num, difference)

    hidden_index = randint(HIDDEN_INDEX_MIN, HIDDEN_INDEX_MAX)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))

    return question, correct_answer
