# Dev app function at home
# Developement at office and forget to push to github
from typing import List 

def binary_search(nums: List, target: int) -> int:
    # open range
    left, right = -1, len(nums) + 1
    while left + 1 < right:
        mid = left + right >> 1
        if nums[mid] < target:
            left = mid 
        else:
            right = mid 
    return left 

# Dev app function at home