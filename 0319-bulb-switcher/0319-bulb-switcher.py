class Solution:
    def bulbSwitch(self, n: int) -> int:
        i=1
        count=0
        while i*i<=n:
            count+=1
            i+=1
        return count    
      