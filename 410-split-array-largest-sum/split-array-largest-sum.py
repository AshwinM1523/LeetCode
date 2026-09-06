class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left = max(nums)
        right = sum(nums)

        while left < right:
            split_sum = left + (right - left) // 2

            splits = 1
            curr = 0

            for num in nums:
                if curr + num > split_sum:
                    splits += 1
                    curr = num
                else:
                    curr += num

            if splits > k:
                left = split_sum + 1
            else:
                right = split_sum

        return left