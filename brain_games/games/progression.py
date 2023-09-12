from brain_games.engine import eng
from brain_games.functions import random_progression


def progression_logic():

    task = 'What number is missing in the progression?'
    questions_lst = list()
    correct_ans_lst = list()

    for i in range(3):
        correct_ans, prog = random_progression()
        correct_ans_lst.append(correct_ans)
        questions_lst.append(' '.join(map(str, prog)))

    eng(task, questions_lst, correct_ans_lst)
