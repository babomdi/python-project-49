def random_progression():
    import random

    prog = []
    num = random.randint(1, 10)
    prog.append(num)
    diff = random.randint(1, 20)

    for i in range(9):
        prog.append(num + diff)
        num = num + diff

    hidden_elem = random.randint(0, 9)
    correct_ans = prog[hidden_elem]
    prog[hidden_elem] = '..'

    return correct_ans, prog
