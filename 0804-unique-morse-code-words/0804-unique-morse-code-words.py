class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lgiven=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d={}
        for i in range(len(lgiven)):
            d[chr(i+97)]=lgiven[i]
        ans=set()
        for i in words:
            t=''
            for j in i:
                t=t+d[j]
            ans.add(t)
        return len(ans)  
        