"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

def solution(s1, s2):
    characters = {}
    count = 0
    
    for letter in s1:
        characters[letter] = characters.get(letter, 0) + 1
        
    for letter in s2:
        if letter in characters and characters[letter] > 0:
            count += 1
            characters[letter] -= 1
    
    return count
            