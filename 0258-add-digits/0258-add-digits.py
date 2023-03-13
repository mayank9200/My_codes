class Solution:
    def addDigits(self, num: int) -> int:
        summ=0
        while num>0:
            summ+=num%10
            num=num//10
        if summ<10:
            return summ
        else:
            return self.addDigits(summ)