class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i,ch in enumerate(word):
            count=Counter(word[:i]+word[i+1:])
            s=set(count.values())
            if(len(s)==1):
                return True
            
        return False