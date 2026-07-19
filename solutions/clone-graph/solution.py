"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
'''
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output:          [[2,4],[1,3],[2,4],[1,3]]

1: 2,4
2: 1,3
3: 2,4
4: 1,3
'''

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]
            if node not in oldtonew:
                copy = Node(node.val)
                oldtonew[node] = copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            return copy

        return dfs(node) if node else None
            
        








        # #dummy = Node(0)
        # clone = Node(node.val)
        # #dummy.neighbors = [clone]

        # clone_neighbors = []
        # for i in range(1,len(node.neighbors)+1):
        #     neigh = node.neighbors[i]
        #     clone_neighbors.append(Node(neigh.val))



        