class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums) - 2):

            # skip duplicate pivots
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            pivot = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr = pivot + nums[left] + nums[right]

                if curr == 0:
                    ans.append([pivot, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr < 0:
                    left += 1
                else:
                    right -= 1

        return ans