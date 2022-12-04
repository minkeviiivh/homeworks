for number in range(1, 101):
<<<<<<< HEAD
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
=======
    if number % 3 == 0 and number % 5 == 0:
        print('FuzzBuzz')
    elif number % 3 == 0:
        print('Fuzz')
    elif number % 5 == 0:
        print('Buzz')
>>>>>>> 6019c970bd3f7be81dc5c0b9866de6646fc927f7
    else:
        print(number)
