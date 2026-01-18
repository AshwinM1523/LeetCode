class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string not in seen:
                seen[sorted_string] = []
            seen[sorted_string].append(s)
        
        output = []
        for value in seen.values():
            output.append(value)
        
        return output
