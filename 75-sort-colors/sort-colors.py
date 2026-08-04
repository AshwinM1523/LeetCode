class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        current = 0
        right = len(nums) - 1

        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1

            elif nums[current] == 1:
                current += 1

            else: 
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1