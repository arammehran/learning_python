def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i

    print("The factorial of {} is {}".format(num, fact))


factorial(20)
"""
You simply need to pass the number which you want to find the factorial of, as an argument while calling the function and that's it!!!
"""
