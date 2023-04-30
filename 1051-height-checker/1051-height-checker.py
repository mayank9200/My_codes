class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=heights.copy()
        expected.sort()
        count=0
        #print(expected,heights)
        for i in range(len(heights)):
            if expected[i]!=heights[i]:
                count+=1
        return count        
            