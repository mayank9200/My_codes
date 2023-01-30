class Solution:
    def compare(self,d1,d2):
        for i in d2:
            if d1[i]<d2[i]:
                return False
        return True    
        
    def minWindow(self, s: str, t: str) -> str:
        d1={}
        d2={}
        for i in t:
            d1[i]=0
            d2[i]=d2.get(i,0)+1
        i=0
        j=0
        n=len(s)
        minn=float('inf')
        val=''
        while j<n:
            while j<n and self.compare(d1,d2)==False:
                if s[j] in d1:
                    d1[s[j]]+=1
                j+=1   
            while i<=j and self.compare(d1,d2)==True:
                if j-i+1<minn:
                    minn=j-i+1
                    val=s[i:j]
                if s[i] in d1:
                    d1[s[i]]-=1
                i+=1    

                
                
                
        return val
        