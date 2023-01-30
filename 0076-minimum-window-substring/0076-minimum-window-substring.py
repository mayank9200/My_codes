class Solution:
    def compare(self,d1,d2):
        for i in d2:
            if d1[i]<d2[i]: #desired number of letters are not yet covered
                return False
        return True  #contains minimum required letters with appropriate frequency
        
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
                if j-i<minn:
                    minn=j-i
                    val=s[i:j]
                if s[i] in d1:
                    d1[s[i]]-=1
                i+=1    

                
                
                
        return val
        