def even():

    import random

    num = random.randint(0, 100)

    if num % 2 == 0:
        correct_ans = 'yes'
    else:
        correct_ans = 'no'

    return correct_ans, num
