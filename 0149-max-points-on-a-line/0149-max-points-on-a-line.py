class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        d={}
        maxx=0
        n=len(points)
        for i in range(n):
            d={}
            for j in range(i+1,n):
                if (points[j][0]-points[i][0])!=0:
                    m=(points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                    d[m]=d.get(m,0)+1
                else:
                    d[float('inf')]=d.get(float('inf'),0)+1    
            for p,q in d.items():
                maxx=max(maxx,q)            
        return maxx+1 