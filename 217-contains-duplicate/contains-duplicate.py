class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numsDict = set()

        for num in nums:
            if num in numsDict:
                return True
            numsDict.add(num)
        
        return False