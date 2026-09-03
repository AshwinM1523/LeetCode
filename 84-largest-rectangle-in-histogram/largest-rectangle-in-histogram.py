class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        max_rect = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()

                width = i - index
                max_rect = max(max_rect, width * h)
                start = index

            stack.append([start, height])

        n = len(heights)

        while stack:
            index, height = stack.pop()

            width = n - index
            max_rect = max(max_rect, width * height)

        return max_rect