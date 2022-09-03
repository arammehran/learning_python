def factorial(num):
    if num == 0 or num == 1:
        return 1
    elif num > 50:
        print('Memeory error.')
    else:
        return num * factorial(num - 1)


result = factorial(7)
print(result)

# if the input is greater than 50, the program prints line 5 statement i.e. Memeory error but it also prints out None. Can you please explain why? 
# output
# Memeory error.
# None
