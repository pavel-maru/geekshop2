#Ok
num = ['',
       'один',
       'два',
       'три',
       'четыре',
       'пять'
]

f_new = open('new_file.txt', 'w')
f = open('my_file.txt', 'r')
while True:
    line = f.readline()
    print(line.strip())
    if line == '':
        break
    words = line.split()
    words[0] = num[int(words[2])]
#   print(words[0])
    line = words[0] + ' ' + words[1] + ' ' + words[2] + '\n'
#   print(line)
    f_new.write(line)

f.close()
f_new.close()
