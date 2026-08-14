class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        left = 0
        right = len(people) - 1
        people.sort()

        while left <= right:
            if left == right:
                ans += 1
                break

            weight = people[right] + people[left]

            if weight > limit:
                # heaviest person goes alone
                ans += 1
                right -= 1
            else:
                # heaviest + lightest go together
                ans += 1
                left += 1
                right -= 1

        return ans