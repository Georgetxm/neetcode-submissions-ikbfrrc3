"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        visited = set()
        start = node

        stack = [start]
        visited.add(start)
        
        while stack:
            node = stack.pop()
            oldToNew[node] = Node(val = node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    stack.append(nei)
                    visited.add(nei)

        for old, new in oldToNew.items():
            for nei in old.neighbors:
                new_nei = oldToNew[nei]
                new.neighbors.append(new_nei)

        return oldToNew[start]
