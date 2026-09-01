class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            x = nums[i]

            if x > 0 and x <= len(nums) and nums[x-1] != x:
                nums[x-1], nums[i] = nums[i], nums[x-1]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return len(nums) + 1

