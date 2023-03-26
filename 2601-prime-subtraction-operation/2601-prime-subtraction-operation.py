class Solution:
    def findprime(self,n):
        ans=[]
        is_prime = [True] * (n+1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(n**0.5)+1):
            if is_prime[p]:
                for i in range(p*p, n+1, p):
                    is_prime[i] = False
        for i in range(2, n+1):
            if is_prime[i]:
                ans.append(i)
        return ans        
    def justgreater(self,primes,val):
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
        primes=self.findprime(1001)
        for i in range(len(nums)-2,-1,-1):
            counter=0
            val=nums[i]
            if nums[i]<nums[i+1]:
                continue
            #print(nums[i])    
            f=self.justgreater(primes,nums[i]-nums[i+1])  
            #print(nums[i]-nums[i+1],f)
            nums[i]=nums[i]-f
        #print(nums)
        if nums[0]<=0:
            return False
        for i in range(1,len(nums)):
            if nums[i]<=0:
                return False
            if nums[i]<nums[i-1]:
                return False
        return True