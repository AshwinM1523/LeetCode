class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # xor
        # xor gets rid of all same numbers making them 0

        res = 0

        for num in nums:
            res ^= num
        
        return res