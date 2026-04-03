class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d={i:[] for i in range(numCourses)}
        for i in prerequisites:
            d[i[0]].append(i[1])

        state=[0]*numCourses
        def dfs(curr):
            #print(curr,state)
            if state[curr]==1:
                return False
            if state[curr]==2:
                return True
            state[curr]=1
            for n in d[curr]:
                if not dfs(n):
                    return False
            state[curr]=2
            return True
        
        for i in d:
            if not dfs(i):
                return False
        return True




        