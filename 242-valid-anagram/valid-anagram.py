class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        seen = {}

        for ch in s:
            if ch not in seen:
                seen[ch] = 0
            seen[ch] += 1
        
        for ch in t:
            if ch not in seen or seen[ch] == 0:
                return False
            seen[ch] -= 1
        
        return True