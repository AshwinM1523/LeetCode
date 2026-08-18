class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) <= 1:
            return False
        
        stack = []
        openpar = set(["(", "[", "{"])

        for i in range(len(s)):
            if s[i] in openpar:
                stack.append(s[i])
                continue
            if len(stack) == 0:
                return False
            curr = stack.pop()
            if curr == "(" and s[i] != ")":
                return False
            if curr == "{" and s[i] != "}":
                return False
            if curr == "[" and s[i] != "]":
                return False
        
        return len(stack) == 0
                
