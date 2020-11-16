class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = [-1]
        for i, num in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > num:
                prev_idx = stack.pop()
                maxarea = max(maxarea, heights[prev_idx] * (i - stack[-1] - 1))
            stack.append(i)
        
        while stack[-1] != -1:
            prev_idx = stack.pop()
            maxarea = max(maxarea, heights[prev_idx] * (i - stack[-1]))
        return maxarea