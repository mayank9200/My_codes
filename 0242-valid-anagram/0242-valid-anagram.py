class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in t:
            if i in d:
                d[i]=d[i]-1
                if d[i]==0:
                    d.pop(i)
            else:
                return False
        if d=={}:    
            return True    
        return False