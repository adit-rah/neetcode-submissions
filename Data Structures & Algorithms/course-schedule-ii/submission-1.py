class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for a,b in prerequisites:
            if a in adj:
                adj[a].append(b)
            else:
                adj[a] = [b]

        res = []
        seen = {}
        def helper(course):
            if course in seen and not seen[course]:
                return False

            if course in seen:
                return True
                
            if course not in adj:
                res.append(course)
                seen[course] = True
                return True
            
            seen[course] = False
            for c in adj[course]:
                if not helper(c):
                    return False
            seen[course] = True
            res.append(course)

            return True
        
        for c in range(numCourses):
            if not helper(c):
                return []
        return res
            
