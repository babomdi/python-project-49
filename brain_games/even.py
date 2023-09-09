def even_logic():
    import prompt
    import random
    from brain_games.cli import welcome_user


    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        num = random.randint(0, 100)
        print('Question:', num)
        ans = prompt.string('Answer: ')
        if num % 2 != 0:
            correct_ans = 'no'
        else:
            correct_ans = 'yes'
        if ans == correct_ans:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{correct_ans}'.")
            print(f"Let's try again, {name}!")
            break
            
