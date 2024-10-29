#syeda khunza fatima
#oct 29th, 2024

#3 this program helps to flip the coin 1000 times, which results in list, and calculates the percentage of "heads" in the list using the "count" method.

#it also helps to calculate the percentage of "heads" based on the count

import random
x = 90
coin_flips =[]
for _ in range(1000):
 if random.randint(1,100) <=x:
    coin_flips.append("heads")
else:
    coin_flips.append("tails")
    heads_count = coin_flips.count("heads")
    tails_count = coin_flips.count("tails")
    heads_percentage = (heads_count / 1000)*100
    print(f"heads appeared {heads_count} times ({heads_percentage}%)")
    print(f"tails appeared {tails_count} times ({100- heads_percentage}%)")
    
