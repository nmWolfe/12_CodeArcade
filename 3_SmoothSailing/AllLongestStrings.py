"""
Given an array of strings, 
return another array containing all of its longest strings.

Example
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
"""

def solution(inputArray):
    returnArray = []
    max_leng = 0
    
    for item in inputArray:
        str_len = len(item)
        if str_len > max_leng:
            max_leng = str_len
            returnArray = [item]
        elif str_len == max_leng:
            returnArray.append(item)
    
    return returnArray