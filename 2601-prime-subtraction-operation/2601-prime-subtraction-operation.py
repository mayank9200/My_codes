class Solution:  
    def findprime(self,n): #print primes upto n
        ans=[]
        for i in range(2,n+1):
            count1=0
            count2=0
            for j in range(2,int(i**0.5)+1):
                count1+=1
                if i%j!=0:
                    count2+=1
            if count1==count2:
                ans.append(i)    
        return ans    
    def justgreater(self,primes,val): #find just greater element in prime using binary search
        start=0
        end=len(primes)-1
        candi=primes[0]
        while start<=end:
            mid=(start+end)//2
            if primes[mid]<=val:  
                start=mid+1
            else:
                candi=primes[mid]
                end=mid-1
        return candi       
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes=self.findprime(1001) #print primes upto 1000
        for i in range(len(nums)-2,-1,-1):
            counter=0
            val=nums[i]
            if nums[i]<nums[i+1]:  #if already less than dont subtract
                continue  
            f=self.justgreater(primes,nums[i]-nums[i+1])  #see the diff and find value just greater
            nums[i]=nums[i]-f #subtract
        if nums[0]<=0:
            return False
        for i in range(1,len(nums)): #see if the array is strictly decreasing
            if nums[i]<=0:
                return False
            if nums[i]<nums[i-1]:
                return False
        return True