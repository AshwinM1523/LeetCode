class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left = max(weights)
        right = sum(weights)
        ans = float("inf")

        while left <= right:
            capacity = (left + right) // 2

            curr_weight = 0
            curr_day = 0

            for i in range(len(weights)):
                curr_weight += weights[i]

                if curr_weight > capacity:
                    curr_day += 1
                    curr_weight = weights[i]

            if curr_weight > 0:
                curr_day += 1

            if curr_day <= days:
                ans = capacity
                right = capacity - 1
            else:
                left = capacity + 1
        
        return ans