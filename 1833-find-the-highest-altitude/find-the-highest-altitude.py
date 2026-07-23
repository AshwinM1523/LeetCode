class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        cur = 0
        high = cur
        for i in range(len(gain)):
            cur += gain[i]

            high = max(cur, high)
        
        return high