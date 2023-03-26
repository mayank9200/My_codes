class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        count=0
        if numOnes!=0:
            if k//numOnes!=0:
                count+=numOnes*1
                k=k-numOnes
            else:
                count+=k*1
                return count
        if numZeros!=0:
            if k//numZeros!=0:
                count+=numZeros*0
                k=k-numZeros
            else:
                count+=k*0
                return count
        count+=k*-1
        return count
            
        