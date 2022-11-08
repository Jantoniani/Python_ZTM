import random
import sys

help(random)

print(dir(random))

print(random.random())

print(random.randint(1,10))

print(random.choice([1, 2, 3, 4, 5, 6, 7]))


my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

sys.argv
