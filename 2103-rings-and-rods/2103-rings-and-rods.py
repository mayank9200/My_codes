class Solution:
    def countPoints(self, rings: str) -> int:
        #easy
        i=0
        n=len(rings)
        ans=0
        d={}
        while i<n:
            a=rings[i]
            b=rings[i+1]  
            if b in d:
                d[b].add(a)
            else:
                d[b]=set(a)
            i+=2    
        #print(d)    
        for i in d:
            if len(d[i])==3:
                ans+=1
        return ans        
        