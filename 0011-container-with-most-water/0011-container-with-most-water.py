class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        maxx=0
        while i<j:
            maxx=max(maxx,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i+=1
            elif height[i]>height[j]:
                j-=1
            else:
                i+=1
                j-=1
        return maxx        
                
                     
                
        
        