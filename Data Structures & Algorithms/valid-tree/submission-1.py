class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import deque, defaultdict
        adj_list = defaultdict(list)

        for e in edges:
            n1, n2 = e
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False

            visit.add(node)

            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n

        # visit = set()
        # q = deque([(0, -1)])
        # visit.add(0)

        # while q:
        #     cur, parent = q.popleft()
        #     for nei in adj_list[cur]:
        #         # undirected edges in adj_list points to itself
        #         if nei == parent:
        #             continue
        #         # one of the neighbour is currently in the visit path
        #         #  i.e. there are cycles
        #         if nei in visit:
        #             return False
        #         q.append((nei, cur))
        #         visit.add(nei)
            
        # return len(visit) == n
                
        