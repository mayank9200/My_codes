class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        from collections import deque
        for i in nums1:
            d[i]=0
        st=deque()
        ans=[]
        for i in range(len(nums2)-1,-1,-1):
            if nums2[i] in d:
                if len(st)>0 and st[0]>nums2[i]:
                    d[nums2[i]]=st[0]
                else:
                    while len(st)>0 and st[0]<nums2[i]:
                        st.popleft()
                    if len(st)==0:
                        d[nums2[i]]=-1
                    else:
                         d[nums2[i]]=st[0]
            st.appendleft(nums2[i])  
        ans=[]
        for i in nums1:
            ans.append(d[i])
        return ans    
            
        