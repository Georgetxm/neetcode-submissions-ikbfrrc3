class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import deque, defaultdict
        adj_list = defaultdict(list)

        for e in edges:
            n1, n2 = e
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visit = set()
        q = deque([(0, -1)])
        visit.add(0)

        while q:
            cur, parent = q.popleft()
            for nei in adj_list[cur]:
                # undirected edges in adj_list points to itself
                if nei == parent:
                    continue
                if nei in visit:
                    return False
                q.append((nei, cur))
                visit.add(nei)
            
        return len(visit) == n
                
        