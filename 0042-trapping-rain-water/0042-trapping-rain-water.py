class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left=[0]*n
        max_right=[0]*n
        ans=0
        for i in range(1,n):
            max_left[i]=max(max_left[i-1],height[i-1])
        for i in range(n-2,0,-1):
            max_right[i]=max(max_right[i+1],height[i+1])    
        for i in range(n):
            ans=ans+max(min(max_left[i],max_right[i])-height[i],0)
        return ans   
            
        
        