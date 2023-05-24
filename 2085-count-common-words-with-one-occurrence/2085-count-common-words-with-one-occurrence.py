class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        #do again
        w1,w2,r = words1 , words2 , 0
        for i in w1:
            if w1.count(i) == w2.count(i) == 1:
                r += 1
        return r
        