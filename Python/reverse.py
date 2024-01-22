''' Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
 _My name is Michele_
Then I would see the string:
 _Michele is name My_
shown back to me.  '''

def reverse_word_order():
    user_string = input('Enter a string: ')
    split_string = user_string.split()
    reversed_string = " ".join(reversed(split_string))
    print(reversed_string)

# Example Usage
reverse_word_order()

