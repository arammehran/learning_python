def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i

    print("The factorial of {} is {}".format(num, fact))


factorial(20)
