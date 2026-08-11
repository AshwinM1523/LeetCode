class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        curr = 0
        ans = 0

        for n in nums:
            curr += n

            # How many previous prefix sums would make
            # the subarray ending here sum to k?
            ans += prefix_count[curr - k]

            # Record this prefix sum
            prefix_count[curr] += 1

        return ans


