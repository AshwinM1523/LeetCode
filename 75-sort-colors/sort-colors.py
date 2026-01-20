class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        freq = {0:0, 1:0, 2:0}

        for num in nums:
            freq[num] += 1
        
        for i in range(len(nums)):
            if freq[0] != 0:
                nums[i] = 0
                freq[0] -= 1
            elif freq[1] != 0:
                nums[i] = 1
                freq[1] -= 1
            else:
                nums[i] = 2
                freq[2] -= 1      
