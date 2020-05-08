"""
https://leetcode-cn.com/problems/cousins-in-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    # 逐层遍历
    def __init__(self):
        self.parent = {}
        self.depth = {}

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.dfs(root)
        return self.depth[x] == self.depth[y] and self.parent[x] != self.parent[y]

    def dfs(self, node, par=None):
        if node:
            self.depth[node.val] = 1 + self.depth[par.val] if par else 0
            self.parent[node.val] = par
            self.dfs(node.left, node)
            self.dfs(node.right, node)


if __name__ == '__main__':
    s = Solution()

    root_ = TreeNode(1)
    g1_2 = TreeNode(2)
    g1_3 = TreeNode(3)
    root_.left = g1_2
    root_.right = g1_3

    g2_4 = TreeNode(4)
    g2_5 = TreeNode(5)
    g1_2.right = g2_4
    g1_3.right = g2_5
    # [1, 2, 3, null, 4, null, 5]

    print(s.isCousins(root_, 4, 5))
