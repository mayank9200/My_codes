class Solution:
    def par(self,i,parent):
        if parent[i]==i:
            return i
        return self.par(parent[i],parent)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        dist=[]
        parent=[i for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                val=abs(points[j][1]-points[i][1])+abs(points[j][0]-points[i][0])
                dist.append([val,i,j])
        dist.sort(key=lambda a:a[0])
        ans=0
        for node in dist:
            val,i,j=node
            p1=self.par(i,parent)
            p2=self.par(j,parent)
            if p1!=p2:
                parent[p2]=p1
                ans=ans+val
         
        return ans        
            
        