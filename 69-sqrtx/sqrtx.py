class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x

        left = 0
        right = x // 2

        while left <= right:
            mid = (left + ((right - left + 1) // 2))
            if x == mid*mid:
                return mid
            elif mid*mid > x:
                right = mid - 1
            else:
                left = mid + 1
        
        return right
            
