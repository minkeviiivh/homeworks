for number in range(1, 101):
    if number % 3 == 0:
        if number % 3 == 0 and number % 5 == 0:
            print('FuzzBuzz')
        else:
            print('Fuzz')
    elif number % 5 == 0:
        if number % 3 == 0 and number % 5 == 0:
            print('FuzzBuzz')
        else:
            print('Buzz')
    else:
        print(number)
