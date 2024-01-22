'''Wikipedia: The regular paperfolding sequence, also known as the dragon curve sequence, is an infinite automatic sequence of 0s and 1s defined as the limit of the following process:

1
1 1 0
1 1 0 1 1 0 0
1 1 0 1 1 0 0 1 1 1 0 0 1 0 0

At each stage an alternating sequence of 1s and 0s is inserted between the terms of the previous sequence.

Define a generator function paperFold that sequentially generates the values of this sequence.

It will be tested for up to 1 000 000 values. '''

def generate_sequence():
    a = [1] * 1000000

    for i in range(1, 1000000):
        j = i + 1
        while j % 2 == 0:
            j //= 2
        a[i] = int(j % 4 == 1)

    return iter(a)

# Example Usage
result_iterator = generate_sequence()
for _ in range(10):
    print(next(result_iterator))

