class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seen = {}

        for ch in s:
            if ch not in seen:
                seen[ch] = 0
            seen[ch] += 1
        
        for ch in t:
            if ch not in seen:
                return False
            seen[ch] -= 1
        
        for key, value in seen.items():
            if value != 0:
                return False
        
        return True