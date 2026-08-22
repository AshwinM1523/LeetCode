class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        ans = float("inf")
        piles.sort()

        while left <= right:
            k = (left + right) // 2

            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / k)
            
            if time <= h:
                ans = k
                right = k - 1
            else:
                left = k + 1
        
        return ans
