class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        n=len(s)
        d=set()
        maxx=0
        while j<n:
            if s[j] not in d:
                d.add(s[j])
                maxx=max(maxx,j-i+1)
                j+=1
            else:
                while s[j]!=s[i]:
                    d.remove(s[i])
                    i+=1
                d.add(s[j])
                i+=1
                j+=1
            #print(d)    
        return maxx        
        