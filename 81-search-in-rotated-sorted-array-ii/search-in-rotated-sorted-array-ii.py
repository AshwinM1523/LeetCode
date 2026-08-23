class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True

            # Duplicates make it impossible to tell
            # which side is sorted
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            
            # Left side is sorted
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            # Right side is sorted
            else:
                if target > nums[r] or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False