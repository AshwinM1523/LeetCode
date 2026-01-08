class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        dup = nums[0]
        while slow != dup:
            slow = nums[slow]
            dup = nums[dup]
        
        return dup