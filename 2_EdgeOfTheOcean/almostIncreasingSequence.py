"""
Given a sequence of integers as an array, 
determine whether it is possible to obtain a strictly increasing sequence 
by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing 
if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.
"""

def solution(sequence):
    count = 0  # Number of elements to remove
    
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            count += 1
            if count > 1:
                return False
            
            # Check both options
            if i > 0 and sequence[i - 1] >= sequence[i + 1]:
                # Remove current element
                if i < len(sequence) - 2 and sequence[i] >= sequence[i + 2]:
                    return False
            else:
                # Remove next element
                if i < len(sequence) - 2 and sequence[i + 1] >= sequence[i + 2]:
                    return False
    
    return True