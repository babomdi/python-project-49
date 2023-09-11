def progression_logic():

    from brain_games.engine import eng
    from brain_games.progression_build import random_progression

    task = 'What number is missing in the progression?'
    questions_lst = []
    correct_ans_lst = []

    for i in range(3):
        correct_ans, prog = random_progression()
        correct_ans_lst.append(str(correct_ans))

        questions_lst.append(' '.join(map(str, prog)))

    eng(task, questions_lst, correct_ans_lst)
