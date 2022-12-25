class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for i in nums:
            xor=xor^i
        rmsb=xor&(-xor) #or rmsb(right most set bit mask)=xor&(~xor+1),ie. number and its 2s compliment
        res1=0
        res2=0
        for i in nums:
            if i&rmsb:
                res1=res1^i
            else:
                res2=res2^i
        return [res1,res2]        