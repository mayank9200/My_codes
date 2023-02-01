class Solution:
    def nsr(self,nums):
        from collections import deque
        s=deque()
        arr=[]
        n=len(nums)
        for i in range(n-1,-1,-1):
            while len(s)>0 and nums[s[0]]>=nums[i]:
                s.popleft()
            if len(s)==0:
                arr.append(len(nums))
            else:
                arr.append(s[0])
            s.appendleft(i)
        return arr[::-1]
    
    def nsl(self,nums):
        from collections import deque
        s=deque()
        arr=[]
        n=len(nums)
        for i in range(n):
            while len(s)>0 and nums[s[0]]>=nums[i]:
                s.popleft()
            if len(s)==0:
                arr.append(-1)
            else:
                arr.append(s[0])
            s.appendleft(i)
        return arr
            
        
    def maxSumMinProduct(self, nums: List[int]) -> int:
        a1=self.nsr(nums)
        a2=self.nsl(nums)
        n=len(nums)
        summ=0
        pre=[]
        maxx=0
        for i in range(n):
            summ=summ+nums[i]
            pre.append(summ)      
        for i in range(n):
            id1=a1[i]-1
            id2=a2[i]+1
            if id2==0:
                reqsum=pre[id1]
            else:
                reqsum=pre[id1]-pre[id2-1] 
            #print(print(reqsum,nums[i]))
            maxx=max(maxx,reqsum*nums[i])    
        return maxx%(pow(10,9)+7)    
        