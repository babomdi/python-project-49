def is_prime():

    import random

    num = random.randint(1, 100)

    if num > 1:
        for i in range(1, num):
            if i > 1 and num % i == 0:
                correct_ans = 'no'
                break
            else:
                correct_ans = 'yes'
    else:
        correct_ans = 'no'

    return correct_ans, num
