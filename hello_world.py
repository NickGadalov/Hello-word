def hello_world():
    print("\nHelo, everyone! Type 'HELLO WORLD!' in this program: ")

    while True:
        message = input()
        if message == 'HELLO WORLD!':
            print('CONGRATULATIONS!')
            return
        else:
            print('You made a mistake, try again!')
            continue

hello_world()