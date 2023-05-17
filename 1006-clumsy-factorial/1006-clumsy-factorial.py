class Solution:
    def clumsy(self, n: int) -> int:
        #do again
        if n <= 2:
            return n
        if n <= 4:
            return n + 3
        
        if (n - 4) % 4 == 0:
            return n + 1
        elif (n - 4) % 4 <= 2:
            return n + 2
        else:
            return n - 1       
            