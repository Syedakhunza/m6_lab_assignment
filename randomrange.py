#syeda khunza fatima
#oct 29th, 2024

#1. this program print random integers between 25-35 using the randrange function

# this give us 10 random intergers at the end of the program

import random
rand_nums = []
for _ in range(10):
    num = random.randrange(25,36)
    rand_nums.append(num)
    print(num)
    print("list of random numbers:", rand_nums)