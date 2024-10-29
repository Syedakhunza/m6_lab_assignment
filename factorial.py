#syeda khunza fatima
# 0ct 29th, 2024

#4 This program help us to calculate the factorial two ways

#it compares the result of both to ensure if they both are same.

import math
num = int(input("enter a number to calculate its factorial:"))
math_factorial = math.factorial(num)
loop_factorial = 1
for i in range(1, num + 1):
    loop_factorial *= i
    print(f"factorial using math.factorial: {math_factorial}")
    print(f"factorial using for loop:{loop_factorial}")
    #compare the two results
    if math_factorial == loop_factorial:
        print("both methods give the same result.")
    else:
        print("the methods give different results.")
        