class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        ans = 0
        left = 0
        right = len(people) - 1
        people.sort()

        while left <= right:
            weight = people[right] + people[left]
            if weight > limit:
                ans += 1
                right -= 1
            else:
                ans += 1
                left += 1
                right -= 1
        
        return ans