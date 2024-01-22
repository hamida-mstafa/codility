def solution(S):
    # Solve for odd / even
    # ?0?, vv, bom
    half_s = len(S) // 2 # Halfway through the string
    palindromeS = S
    # check if middle character (if string is odd length) is a ?
    if len(S) % 2 == 1 and palindromeS[half_s] == "?":
        palindromeS = palindromeS[:half_s] + "a" + palindromeS[half_s+1:]
    # loop from back and front, inwards
    for start_index in range(0, half_s):
        start_char = S[start_index] # start indexing at 0
        end_index = - (start_index + 1) # start indexing at -1
        end_char = S[end_index]
        if end_char == "?" and start_char == "?":
            # replace both ? with a character . i.e ?o? -> aoa
            palindromeS = palindromeS[:start_index] + "a" + palindromeS[start_index+1:]
            # are we at -1
            if end_index == -1:
                palindromeS = palindromeS[:end_index] + "a"
            else:
                palindromeS = palindromeS[:end_index] + "a" + palindromeS[end_index+1:]
            continue # todo, find sol
        elif end_char == "?":
            # replace ? at start with end character. i.e bo? -> bob
            # are we at -1? then don't append anything
            if end_index == -1:
                palindromeS = palindromeS[:end_index] + palindromeS[start_index]
            else:
                palindromeS = palindromeS[:end_index] + palindromeS[start_index] + palindromeS[end_index+1:]
            continue
        elif start_char == "?":
            # replace ? at start with end character. i.e ?om -> mom
            palindromeS = palindromeS[:start_index] + palindromeS[end_index] + palindromeS[start_index+1:]
            continue
        else:
            if end_char != start_char:
                return "NO"
            else:
                # works as a palindrome
                continue
    return palindromeS