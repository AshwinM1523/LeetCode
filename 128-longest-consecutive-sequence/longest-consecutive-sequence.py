class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        ans = 0

        for num in seen:
            total = 0
            if num - 1 not in seen:
                start = num
                while start in seen:
                    total += 1
                    start += 1
            ans = max(ans, total)
        
        return ans
