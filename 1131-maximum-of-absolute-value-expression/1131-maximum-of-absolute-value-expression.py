class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        maxx=float(-inf)
        mx1,mx2,mx3,mx4=float('-inf'),float('-inf'),float('-inf'),float('-inf')
        mn1,mn2,mn3,mn4=float('inf'),float('inf'),float('inf'),float('inf')
        for i in range(len(arr1)):
            mx1=max(mx1,arr1[i]+arr2[i]+i)
            mn1=min(mn1,arr1[i]+arr2[i]+i)
            ans1=mx1-mn1
            mx2=max(mx2,-arr1[i]+arr2[i]+i)
            mn2=min(mn2,-arr1[i]+arr2[i]+i)
            ans2=mx2-mn2
            mx3=max(mx3,arr1[i]-arr2[i]+i)
            mn3=min(mn3,arr1[i]-arr2[i]+i)
            ans3=mx3-mn3
            mx4=max(mx4,-arr1[i]-arr2[i]+i)
            mn4=min(mn4,-arr1[i]-arr2[i]+i)
            ans4=mx4-mn4
        return max([ans1,ans2,ans3,ans4])      
            
        