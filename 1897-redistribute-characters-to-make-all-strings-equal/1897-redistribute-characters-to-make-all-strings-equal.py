class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d={}
        for i in words:
            for j in i:
                d[j]=d.get(j,0)+1
        for i,j in d.items():
            if j%len(words)!=0:
                return False
        return True    
        