class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=0
        summ=0
        for i in range(1,n+1):
            summ+=i
            if summ>n:
                return i-1
        return 1    