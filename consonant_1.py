def solve(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
              'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
              't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    
    substrings = []
    current_substring = ''
    max_value = 0
    
    for char in s:
        if char in consonants:
            current_substring += char
        else:
            if current_substring:
                substring_value = sum(values[c] for c in current_substring)
                max_value = max(max_value, substring_value)
                substrings.append(current_substring)
                current_substring = ''
    
    if current_substring:
        substring_value = sum(values[c] for c in current_substring)
        max_value = max(max_value, substring_value)
        substrings.append(current_substring)
    
    return max_value


print(solve("zodiacs"))   
print(solve("strength"))  
print(solve("Trichotillomania."))
print(solve("Hippopotomonstrosesquippedaliophobia"))
