class Solution:
    
       
        
                
        
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #LIS solution that is easy
        # envelopes.sort()
        # n=len(envelopes)
        # dp=[0 for i in range(n)]
        # dp[0]=1
        # n=len(envelopes)
        # for i in range(1,n):
        #     maxx=0
        #     for j in range(i):
        #         if envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1]:
        #             maxx=max(maxx,dp[j])
        #     dp[i]=maxx+1
        # return max(dp)        
        
        #trying with help of binary search with LIS
        def binarysearch(arr,val):
            n=len(arr)
            start=0
            end=len(arr)-1
            if len(arr)==0 or arr[-1]<val:
                arr.append(val)
                return 
            candi=0
            while start<=end:
                mid=(start+end)//2
                if arr[mid]==val:
                    return
                elif arr[mid]>val:
                    candi=mid
                    end=mid-1
                else:
                    start=mid+1
            arr[candi]=val
            return
            
        envelopes.sort(key= lambda a:(a[0], -a[1]))
        arrheight=[]
        lis=[]
        n=len(envelopes)
        for i in range(n):
            arrheight.append(envelopes[i][1])
        for i in range(n):
            binarysearch(lis,arrheight[i])   
        return len(lis)
        
        
                
        
        