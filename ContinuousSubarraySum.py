from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the first occurrence of each remainder
        remainder_index_map = {0: -1}
        cumulative_sum = 0
        
        for i, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k
            
            if remainder in remainder_index_map:
                if i - remainder_index_map[remainder] > 1:
                    return True
            else:
                remainder_index_map[remainder] = i
        
        return False