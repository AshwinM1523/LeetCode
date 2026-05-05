class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        numMap = {}

        for i in range(len(nums)):
            if nums[i] in numMap:
                if abs(i - numMap[nums[i]]) <= k:
                    return True
            numMap[nums[i]] = i

        return False
            
                