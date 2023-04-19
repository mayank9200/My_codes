class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        from collections import deque
        q=deque()
        q.append([id,0])
        visited=[False for i in range(len(watchedVideos))]
        visited[id]=True
        ans=[]
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node,lev=q.popleft()
                if lev>level:
                    break
                if lev==level:
                    ans.append(node)
                for j in friends[node]:
                    if visited[j]==False:
                        q.append([j,lev+1])
                        visited[j]=True
        d={}
        fans=[]
        for i in ans:
            for j in watchedVideos[i]:
                d[j]=d.get(j,0)+1
        tans=[]
        for i in d:
            tans.append([d[i],i])
        tans.sort()
        for i in tans:
            fans.append(i[1])
        return fans    
                         
            
        