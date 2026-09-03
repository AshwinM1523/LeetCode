class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        i = 0
        max_rect = 0

        while i < len(heights):
            if (stack and stack[-1][1] <= heights[i]) or not stack:
                stack.append([i, heights[i]])
                i += 1
                continue
            while stack and stack[-1][1] > heights[i]:
                curr_rect_index, curr_rect_height = stack.pop()

                area = (i - curr_rect_index) * curr_rect_height
                max_rect = max(max_rect, area)
                start = curr_rect_index

            stack.append([start, heights[i]])
            i += 1

        while stack:
            curr_rect = stack.pop()
            curr_rect_index = curr_rect[0]
            curr_rect_height = curr_rect[1]

            area = (i - curr_rect_index) * curr_rect_height
            max_rect = max(max_rect, area)
        
        return max_rect


