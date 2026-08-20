class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures) 
        stack = []
        indices = []

        for i in range(len(temperatures)):
            while stack and stack[-1] < temperatures[i]:
                stack.pop()
                curr = indices.pop()
                ans[curr] = i - curr
            stack.append(temperatures[i])
            indices.append(i)
        
        return ans