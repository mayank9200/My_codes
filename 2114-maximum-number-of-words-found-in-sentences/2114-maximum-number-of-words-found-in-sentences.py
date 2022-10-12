class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxx=0
        for i in sentences:
            count=0
            for j in i:
                if j==' ':
                    count+=1
            maxx=max(maxx,count+1)
        return maxx    
            
        