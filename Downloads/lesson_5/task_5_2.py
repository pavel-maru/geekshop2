#Uk
with open('user_text.txt', 'r') as file:

    lines = file.readlines()
#   print(lines)
    print(f'Number of lines in the file: {len(lines)}')
    for line in lines:
        words = line.split()
        print(f'Number of words in the string: {len(words)}')
