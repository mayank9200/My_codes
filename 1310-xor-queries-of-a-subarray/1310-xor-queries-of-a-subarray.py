class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre=[0]*len(arr)
        pre[0]=arr[0]
        n=len(arr)
        for i in range(1,n):
            pre[i]=pre[i-1]^arr[i]
        pre.append(0)
        ans=[]
        print(pre)
        for i in queries:
            ans.append(pre[i[1]]^pre[i[0]-1])
        return ans    