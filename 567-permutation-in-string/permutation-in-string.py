class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        count = Counter(s1)
        perms = defaultdict(int)
        left = 0

        for right in range(len(s2)):
            perms[s2[right]] += 1
            while right - left + 1 > len(s1):
                perms[s2[left]] -= 1
                if perms[s2[left]] == 0:
                    del perms[s2[left]]
                left += 1
            if perms == count:
                return True
        return False
                

