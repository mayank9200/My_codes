#User function Template for python3

class Solution:
    def findOrder(self,alien_dict, N, K):
        from collections import deque
        q=deque()
        ans=[]
        adj={}
        indegree={}
        for i in range(97,97+K):
            adj[chr(i)]=[]
            indegree[chr(i)]=0
        for i in range(1,N):
            s1=alien_dict[i-1]
            s2=alien_dict[i]
            p1,p2=0,0
            while p1<len(s1) and p2<len(s2):
                if s1[p1]!=s2[p2]:
                    adj[s1[p1]].append(s2[p2])
                    indegree[s2[p2]]+=1
                    break
                p1+=1
                p2+=1
                        
        for i in adj:
            if indegree[i]==0:
                q.append(i)
        #print(q)        
        while len(q)>0:
            val=q.popleft()
            ans.append(val)
            for i in adj[val]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        #print(ans)
        return ans            
                
            
    # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends