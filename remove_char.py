# Write a program to remove characters from a string starting from zero up to n and return a new string.

# https://pynative.com/python-basic-exercise-for-beginners/
# Exercise 4. Please compare my solution with the one on the above link. I didn't use function. And I used a different method to solve it. i am not sure if it;s good or not. 


word = input('Enter a word: \n')
n = int(input("n is: \n"))
size = len(word)
if n > size:
    print("Error! n must be less than the length of the string.")
else: 
    print(word)
    print(word[n:])
