"""
Given an array of integers, 
find the pair of adjacent elements that has the 
largest product and return that product.
"""

def solution(inputArray):
    max_value = float('-inf')
    for num in range(len(inputArray) - 1):
        pair_value = inputArray[num] * inputArray[num+1]
        if pair_value > max_value:
            max_value = pair_value
    return max_value