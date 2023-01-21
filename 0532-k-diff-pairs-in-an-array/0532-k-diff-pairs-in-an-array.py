class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         i=0
#         j=1
#         count=0
#         n=len(nums)
#         while j<n:
#             #print(i,j)
#             if nums[j]-nums[i]==k:
#                 count+=1
#                 t1=nums[j]
#                 t2=nums[i]
#                 while j<n-1 and nums[j]==t1:
#                     j+=1
#                 while i<n-1 and nums[i]==t2:
#                     i+=1
#             elif nums[j]-nums[i]>k:
#                 i+=1
#             else:
#                 j+=1
#             if i==j:
#                 j+=1              
#         return count
          d={}
          count=0
          for i in nums:
            d[i]=d.get(i,0)+1
          if k==0:
            for i in d:
                if d[i]>1:
                    count+=1
          else:           
            for i in d:
                if i-k in d:
                    count+=1
          return count              
                
            
           
        
        