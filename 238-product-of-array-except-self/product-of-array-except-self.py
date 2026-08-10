class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(ans[i - 1] * nums[i])
            
        suffix = 1
        for i in range(len(nums) - 1, 0, -1):
            ans[i] =  ans[i-1] * suffix
            suffix *= nums[i]
        ans[0] = suffix
        
        return ans