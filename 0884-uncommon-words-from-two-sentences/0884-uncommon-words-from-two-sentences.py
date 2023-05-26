class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        a1=s1.split(' ')
        a2=s2.split(' ')
        d1={}
        d2={}
        for i in a1:
            d1[i]=d1.get(i,0)+1
        for i in a2:
            d2[i]=d2.get(i,0)+1
        ans=[]
        for i in a1:
            if i not in d2 and d1[i]==1:
                ans.append(i)
        for i in a2:
            if i not in d1 and d2[i]==1:
                ans.append(i)
        return ans        