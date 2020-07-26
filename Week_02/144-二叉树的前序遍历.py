#Leetcode 144

#解法一
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        def helper(root):
            return [root.val] + helper(root.left) + helper(root.right) if root else []
        output = helper(root)
        return output


#解法二，把解法一展开
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        def helper(root):
            if not root: return None
            output.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return output

#解法三，用栈，把左右节点反转后放入栈，取出后左节点先出，满足条件。
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res



















