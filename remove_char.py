# Write a program to remove characters from a string starting from zero up to n and return a new string.


word = input('Enter a word: \n')
n = int(input("n is: \n"))
size = len(word)
if n > size:
    print("Error! n must be less than the length of the string.")
else: 
    print(word)
    print(word[n:])
