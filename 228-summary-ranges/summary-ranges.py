class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        ans = []
        left = 0
        for right in range(1, len(nums)):
            if nums[right] - 1 != nums[right-1]:
                if left == right - 1:
                    ans.append(f"{nums[left]}")
                else:
                    ans.append(f"{nums[left]}->{nums[right - 1]}")
                left = right
        
        if nums:
            if left == len(nums) - 1:
                ans.append(str(nums[left]))
            else:
                ans.append(f"{nums[left]}->{nums[-1]}")

        return ans