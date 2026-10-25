class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights)-1
        result = 0

        def calculateSize(n1, n2):
            return (min(heights[n1],heights[n2]) *(n2-n1))

        while left < right:
            print(result)
            size = calculateSize(left, right)
            if result < size:
                result = size

            if min(heights[left],heights[right]) == heights[left]:
                left += 1
            else:
                right -= 1
        return result
                

            