'''Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
The goal of this exercise is to think about some internals that Python normally takes care of for us. All you need is some variables and if statements! '''
def large_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(num1)
        return num1
    elif num2 > num3 and num2 > num1:
        return num2
    else:
        print(num3)
        return num3

# Example Usage
result = large_num(5, 8, 3)
print("The largest number is:", result)

