class Solution:
    from collections import deque
    def nsr(self,arr):
        s=deque()
        ans=[]
        n=len(arr)
        for i in range(n-1,-1,-1):
            if len(s)>0 and arr[s[0]]<arr[i]:
                ans.append(s[0])
            else:
                while len(s)>0 and arr[s[0]]>=arr[i]:
                    s.popleft()
                if len(s)==0:
                    ans.append(len(arr))
                else:
                    ans.append(s[0])
            s.appendleft(i)        
        return ans[::-1]
    def nsl(self,arr):
            s=deque()
            ans=[]
            n=len(arr)
            for i in range(n):
                if len(s)>0 and arr[s[0]]<arr[i]:
                    ans.append(s[0])
                else:
                    while len(s)>0 and arr[s[0]]>=arr[i]:
                        s.popleft()
                    if len(s)==0:
                        ans.append(-1)
                    else:
                        ans.append(s[0])
                s.appendleft(i)        
            return ans
    def largestRectangleArea(self, heights: List[int]) -> int:
        a1=self.nsl(heights)
        a2=self.nsr(heights)
        maxx=0
        for i in range(len(heights)):
            maxx=max(maxx,(a2[i]-a1[i]-1)*heights[i])
        return maxx
        