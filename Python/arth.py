'''This is the first part of this kata series. Second part is here and third part is here

  Add two English words together!

  Implement a class Arith such that

    var k = new Arith("three");
    k.add("seven");  this should return "ten"
  Input - Will be between zero and ten and will always be in lower case

  Output - Word representation of the result of the addition. Should be in lower case'''

class Arith:
    def __init__(self, word):
        self.val = map.index(word)

    def add(self, word):
        return map[map.index(word) + self.val]

map = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
       "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
       "seventeen", "eighteen", "nineteen", "twenty"]

# Example Usage
calculator = Arith("three")
result = calculator.add("four")
print(result)  # Output: seven
