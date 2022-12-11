class Solution:
    def reverseBits(self, n: int) -> int:
        num=0
        for i in range(32):
            if (n>>i)&1:
                num=num|(1<<(31-i))
        return num       
        