class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d={}
        for i in range(len(arr)):
            arr[i]=arr[i]%k
            d[arr[i]]=d.get(arr[i],0)+1
        count=0    
        if 0 in d:
            if d[0]%2!=0:
                return False
            else:
                count=count+d[0]//2
                d.pop(0)
        for i in arr:
            if len(d)==0:
                break    
            if k-i in d:
                count+=1
                if i not in d:
                    return False
                d[i]-=1
                if d[i]==0:
                    d.pop(i)
                if k-i not in d:
                    return False
                d[k-i]-=1
                if d[k-i]==0:
                    d.pop(k-i)
        if count==len(arr)//2:
            return True
        else:
            return False
                
         
        