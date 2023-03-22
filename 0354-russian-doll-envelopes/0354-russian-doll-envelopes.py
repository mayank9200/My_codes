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
        #https://www.youtube.com/watch?v=DnR_k51J5PM
        def binarysearch(arr,val): #function to find number just greater than current
            n=len(arr)
            start=0
            end=len(arr)-1
            if len(arr)==0 or arr[-1]<val: #if array is empty or element is grater than last element then just append
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
            arr[candi]=val #put the value at candidate(value just greater than current)
            return
            
        envelopes.sort(key= lambda a:(a[0], -a[1])) #very important step, sort width in incresing and if width is same than height in decreasing in order to make sure that we can make clear which value to take if heights are same(refer video for better explaination)
        
        #now just apply LIS with binary search on heights as we can see that widths are now managed
        arrheight=[]
        lis=[]
        n=len(envelopes)
        for i in range(n):
            arrheight.append(envelopes[i][1])  #creating height array
        for i in range(n):
            binarysearch(lis,arrheight[i])   #finding lower bound
        return len(lis) #len of lis is the ans
        
        
                
        
        