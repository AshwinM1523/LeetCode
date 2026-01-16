class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seen = {}

        for ch in s:
            if ch not in seen:
                seen[ch] = 0
            seen[ch] += 1
        
        for ch in t:
            if ch not in seen or seen[ch] == 0:
                return False
            seen[ch] -= 1
        
        return all(value == 0 for value in seen.values())