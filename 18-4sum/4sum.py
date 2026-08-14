class Solution:

    def threeSum(self, k, nums, target):
        ans = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            pivot = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr = k + pivot + nums[left] + nums[right]

                if curr == target:
                    ans.append([k, pivot, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr < target:
                    left += 1
                else:
                    right -= 1

        return ans

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            ans.extend(
                self.threeSum(nums[i], nums[i + 1:], target)
            )

        return ans