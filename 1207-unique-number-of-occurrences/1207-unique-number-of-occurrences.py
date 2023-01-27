class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        s=set()
        for i in arr:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            s.add(j)   
        if len(s)==len(d):
            return True
        else:
            return False
            
        