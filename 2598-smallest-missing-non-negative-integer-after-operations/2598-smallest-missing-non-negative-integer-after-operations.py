class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        m = Counter([n % value for n in nums])
        print(m)
        for i in range(len(nums)):
            print(i,value,i%value)
            if m[i % value] == 0:
                return i
            m[i % value] -= 1 
        return len(nums)  
                 
            
        
        
        
        
        
            
        