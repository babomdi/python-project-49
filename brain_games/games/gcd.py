def gcd_logic():

    import random
    import math
    from brain_games.engine import eng

    task = 'Find the greatest common divisor of given numbers.'
    questions_lst = []
    correct_ans_lst = []

    for i in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        questions_lst.append(f'{num1} {num2}')

        correct_ans = str(math.gcd(num1, num2))
        correct_ans_lst.append(correct_ans)

    eng(task, questions_lst, correct_ans_lst)
