class Solution:
    def reverse(self,s):
        arr=[i for i in s]
        i=0
        j=len(arr)-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        return ''.join(arr)    
    def reverseWords(self, s: str) -> str:
        i=0
        j=0
        ans=''
        while j<len(s):
            if s[j]==' ':
                val=self.reverse(s[i:j])
                ans=ans+val+' '
                i=j+1
            j+=1
        return ans+self.reverse(s[i:j])
        