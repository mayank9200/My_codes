class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        #simple level order traversal, where for the level we fing the frequencies of watchedVideos and sort them in ascending order
        #friends is the adjacency list
        from collections import deque
        q=deque()
        q.append([id,0]) #id and its level
        visited=[False for i in range(len(watchedVideos))]
        visited[id]=True
        ans=[]
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node,lev=q.popleft() #
                if lev>level: #exceeded level
                    break
                if lev==level: #reached level
                    ans.append(node)
                for j in friends[node]: #going to all its neighbors
                    if visited[j]==False:
                        q.append([j,lev+1]) 
                        visited[j]=True
        d={}
        fans=[]
        for i in ans:
            for j in watchedVideos[i]:
                d[j]=d.get(j,0)+1 #making frequency hashmap
        tans=[]
        for i in d:
            tans.append([d[i],i]) #appending freq,alphabet
        tans.sort() #sorting them
        for i in tans:
            fans.append(i[1]) #appending the alphabets
        return fans    
                         
            
        