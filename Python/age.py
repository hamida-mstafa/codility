'''Context: Ask a small girl - "How old are you?". She always says strange things... Lets help her!
Task: For correct answer program should return int from 0 to 9. Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only 

bdd
the user should:
input a string
receive a number

input         output
9 years old    9

pseudocode
define a function
take the input from user
loop through the String
return number 
code in python '''
def main():
    age = input("hi little girl how are you?")
    for i in "0123456789":
        if i in age:
            return int(age)
