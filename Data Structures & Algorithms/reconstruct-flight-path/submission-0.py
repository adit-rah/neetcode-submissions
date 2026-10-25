class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True) # lex
        adj = {}

        for fr,to in tickets:
            if fr not in adj:
                adj[fr] = []
            adj[fr].append(to)
        
        # BUF to HOU
        # so we need to put BUF
        # dfs?
        res = []
        def helper(node):
            while node in adj and adj[node]:
                to = adj[node].pop()
                helper(to)
            
            res.append(node)
        
        helper("JFK")
        return res[::-1]