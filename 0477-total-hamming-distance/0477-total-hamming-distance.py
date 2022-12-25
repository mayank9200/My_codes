class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        summ=0
        for i in range(32):
            cones=0
            czeros=0
            for j in nums:
                if j&(1<<i):
                    cones+=1
                else:
                    czeros+=1
            summ+=(cones*czeros)       
        return summ    
                
        