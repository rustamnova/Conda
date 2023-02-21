import random

for i in range(10):
    a = random.randint(-10, 10)
    print("Randomly selected number: ", a)
    if a < -10:
        print('Low')
    elif -10 <= a <= 10:
        print('Mid')
    else:
        print('High')
