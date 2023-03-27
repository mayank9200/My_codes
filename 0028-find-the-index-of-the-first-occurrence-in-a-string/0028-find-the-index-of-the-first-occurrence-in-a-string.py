class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=0
        while i<len(haystack):
            ii=i
            j=0
            while ii<len(haystack) and j<len(needle) and haystack[ii]==needle[j]:
                ii+=1
                j+=1
            if j==len(needle):
                return ii-len(needle)
            i+=1
        return -1    
        