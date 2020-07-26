#Leetcode 589

#解法一,递归，先孩子节点放数组里，再根节点。时间和空间复杂度都是O(N)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return None
        output = []
        def helper(root):
            for i in root.children:
                helper(i)
            output.append(root.val)
        helper(root)
        return output


#解法二，用栈。借鉴N叉树的前序遍历，这里先把根节点放数组里，
#再把子节点不反转就正常顺序放栈里，最后的输出结果是第一个是根节点，
#后面是子节点的反向。这时把数组反转，变成先子节点后是根节点。
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return None
        output = []
        stack = [root]
        while len(stack):
            temp = stack.pop()
            output.append(temp.val)
            stack.extend(temp.children)
        return output[::-1]

        




