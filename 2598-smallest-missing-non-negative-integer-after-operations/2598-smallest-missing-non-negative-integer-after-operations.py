class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        m = Counter([n % value for n in nums]) #creating frequency of min value that it can make
        print(m)
        for i in range(len(nums)):
            if m[i % value] == 0: #starting from 0 see if curr value can be made from element and it has a frequency greater than 0
                return i
            m[i % value] -= 1 #made one element so subtract its frequency
        return len(nums)  
                 
            
        
        
        
        
        
            
        