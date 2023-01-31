class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        ans=[]
        i=0
        j=0
        n=len(nums)
        q=deque()
        while j<n:
            if j-i+1<k:
                while len(q)>0 and nums[j]>q[-1]:
                    q.pop()
                q.append(nums[j])
                j+=1
                 
            else:
                while len(q)>0 and nums[j]>q[-1]:
                    q.pop()   
                q.append(nums[j])
                #print(q)  
                ans.append(q[0])
                if q[0]==nums[i]:
                    q.popleft()
                i+=1
                j+=1
                
        return ans       
                
                
                
        