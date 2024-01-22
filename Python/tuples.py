'''task: You are provided a list of rational numbers that are all positive integers. You have to simplify them and return them in a list of tuples.
Example
Input: [[6, 12], [4, 12], [3, 12]]
Output: [(1,2), (1,3), (1,4)] '''

def translate(word):
    return word if len(word) < 2 else word[1:] + word[0] + "ay" if word[0] not in "aeiou" else word + "ay"

# Example Usage
input_word = "python"
translated_word = translate(input_word)
print(translated_word)

