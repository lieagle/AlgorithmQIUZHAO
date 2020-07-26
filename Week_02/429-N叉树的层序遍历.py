#Leetcode 429

#解法一,层序遍历用BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return None
        output = []
        def bfs(root):
            queue = [root]
            while queue:
                temp1 = []
                temp2 = []
                for node in queue:
                    temp1.append(node.val)
                    for child in node.children:
                        temp2.append(child)
                output.append(temp1)
                queue = temp2
        bfs(root)
        return output
        
        
        