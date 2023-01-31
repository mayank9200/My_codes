class Solution:
    def nsr(self,arr):
        from collections import deque
        s=deque()
        t=[]
        la=len(arr)
        for i in range(la-1,-1,-1):
            if len(s)==0:
                t.append(la)
            elif arr[i]>s[0][0]:
                t.append(s[0][1])
            else:
                while len(s)!=0 and arr[i]<=s[0][0]:
                    s.popleft()
                if len(s)==0:
                    t.append(la)
                else:
                    t.append(s[0][1])
            s.appendleft([arr[i],i])
        return t[::-1]
    
    def nsl(self,arr):
        from collections import deque
        s=deque()
        t=[]
        la=len(arr)
        for i in range(la):
            if len(s)==0:
                t.append(-1)
            elif arr[i]>s[0][0]:
                t.append(s[0][1])
            else:
                while len(s)!=0 and arr[i]<=s[0][0]:
                    s.popleft()
                if len(s)==0:
                    t.append(-1)
                else:
                    t.append(s[0][1])
            s.appendleft([arr[i],i])
        return t      
        
    def mah(self, heights: List[int]) -> int:
        t1=self.nsr(heights)
        t2=self.nsl(heights)
        diff=[]
        area=[]
        for i in range(len(heights)):
            diff.append(t1[i]-t2[i]-1)
        for i in range(len(t1)):
            area.append(diff[i]*heights[i])
        return max(area)
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxx=0
        row=len(matrix)
        col=len(matrix[0])
        arr=[0]*col
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=='0':
                    arr[j]=0
                else:
                    arr[j]+=1
            #print(arr)    
            maxx=max(maxx,self.mah(arr))
        return maxx        
        
        