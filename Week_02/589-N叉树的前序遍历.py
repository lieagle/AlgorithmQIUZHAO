#Leetcode 589

#解法一,递归，先根节点放数组里，再孩子节点
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return None
        output = []
        def helper(root):
            output.append(root.val)
            for i in root.children:
                helper(i)
        helper(root)
        return output


#解法二，用栈。先把根节点放数组里，再把子节点反转都放栈里，抛出时就是正常子节点顺序了。
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return None
        output = []
        stack = [root]
        while len(stack):
            temp = stack.pop()
            output.append(temp.val)
            stack.extend(reversed(temp.children))
        return output
        
        