class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        for num in nums:
            prefix.append(prefix[-1] * num)
        prefix.append(1)
        
        suffix = [1]
        for num in reversed(nums):
            suffix.insert(0, suffix[0] * num)
        suffix.insert(0, 1)
        
        print(suffix)
        print(prefix)
        ans = []
        for i in range(1, len(prefix) - 1):
            ans.append(prefix[i-1] * suffix[i+1])
        
        return ans