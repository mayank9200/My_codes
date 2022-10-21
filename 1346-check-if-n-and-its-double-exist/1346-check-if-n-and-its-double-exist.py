class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s=set()
        count0=0
        for i in range(len(arr)):
            s.add(arr[i])
            if arr[i]==0:
                count0+=1
        if 0 in s and count0<=1:
            s.remove(0)
        for i in range(len(arr)):
            if 2*arr[i] in s:
                print(2*arr[i])
                return True
        return False    
        