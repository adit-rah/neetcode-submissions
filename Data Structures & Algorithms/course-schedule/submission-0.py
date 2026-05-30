class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for a,b in prerequisites:
            if a not in adj:
                adj[a] = [b]
            else:
                adj[a].append(b)

        res = [0] * numCourses

        def dfs(course):
            if res[course] == 1:
                return False
            
            if res[course] == 2:
                return True
            
            res[course] = 1
            if course in adj:
                for c in adj[course]:
                    if not dfs(c):
                        return False
            
            res[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True