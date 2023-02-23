class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        i=len(s)-1
        while i>=0 and s[i]==' ': #remove last spaces
            i-=1
        while i>=0:
            if s[i]!=' ':
                count+=1 #just count
                i-=1
            else:
                break
        return count        
        