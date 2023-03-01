class Solution:
    def sortSentence(self, s: str) -> str:
        d={}
        j=0
        for i in range(len(s)):
            if s[i].isdigit():
                d[int(s[i])-1]=s[j:i]
                j=i+2 
        arr=[0]*len(d)
        for i in d:
            arr[i]=d[i]
        return ' '.join(arr)    
        