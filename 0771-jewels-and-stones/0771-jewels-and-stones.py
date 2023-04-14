class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d={}
        for i in jewels:
            d[i]=d.get(i,0)+1
        count=0
        for i in stones:
            if i in d:
                count+=1
        return count        
        