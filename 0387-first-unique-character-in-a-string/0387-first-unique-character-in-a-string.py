class Solution:
    def firstUniqChar(self, s: str) -> int:
        arr=[-1]*256
        for i in range(len(s)):
            if arr[ord(s[i])]==-1:
                arr[ord(s[i])]=i
            else:
                arr[ord(s[i])]=-2
        for i,j in enumerate(s):
            if arr[ord(j)]!=-1 and arr[ord(j)]!=-2:
                return i
        return -1    
        