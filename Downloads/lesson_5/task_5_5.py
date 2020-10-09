#Ok
from random  import randint
with open('my_num.txt', 'r+') as file:
    for i in range(1, 10):
        num = randint(1, 200)
        file.write(str(num) + ' ')
    line = file.readline()
#print(line)
numbers = line.split()
#print(numbers)
sum = 0
for number in numbers:
    sum = sum + int(number)
print(sum)
