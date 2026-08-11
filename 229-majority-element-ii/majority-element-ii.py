class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        seen = defaultdict(int)

        for n in nums:
            seen[n] += 1
            if len(seen) <= 2:
                continue
            
            new_seen = defaultdict(int)
            for n, c in seen.items():
                seen[n] -= 1
                if c > 1:
                    new_seen[n] = c - 1
            seen = new_seen

        res = []

        for n in seen:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        
        return res