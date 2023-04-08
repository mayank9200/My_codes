class Solution:
    def countSegments(self, s: str) -> int:
#         int res=0;
#     for(int i=0; i<s.length(); i++)
#         if(s.charAt(i)!=' ' && (i==0 || s.charAt(i-1)==' '))
#             res++;        
#     return res;
# }
       
       
        count=0
        for i in range(len(s)):
            if s[i]!=' ' and (i==0 or s[i-1]==' '):
                count+=1
        return count
        