#Ok
with open('user_text.txt', 'w') as file:
    while True:
        user_line = input('Input text: ')
        if user_line == '':
            break
        user_line = user_line + '\n'
        file.write(user_line)
