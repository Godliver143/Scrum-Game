word = input ("What is the word for today:")

if (word == word[::-1]):
    print("Is a Palindrome")
    
else:
    print("Is not a Palindrome,please enter a new word.")
