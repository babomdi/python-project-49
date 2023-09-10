def progression_logic():

    import random
    from brain_games.engine import eng

    task = 'What number is missing in the progression?'
    questions_lst = []
    correct_ans_lst = []

    for i in range(3):
        prog = []
        num = random.randint(1, 10)
        prog.append(num)
        diff = random.randint(1, 20)

        for j in range(9):
            prog.append(num + diff)
            num = num + diff

        hidden_elem = random.randint(0, 9)
        correct_ans = prog[hidden_elem]
        correct_ans_lst.append(str(correct_ans))
        prog[hidden_elem] = '..'

        questions_lst.append(f'{prog[0]} {prog[1]} {prog[2]} {prog[3]} \
{prog[4]} {prog[5]} {prog[6]} {prog[7]} {prog[8]} {prog[9]}')

    eng(task, questions_lst, correct_ans_lst)
