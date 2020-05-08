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
    def __init__(self):
        self._x = None
        self._y = None

    # 暴力法 逐层遍历
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depth = 1
        node_queue = [root]
        while True:
            node_queue = self.layer_traverse(node_queue, depth, x, y)
            if all([self._y == self._x, self._x, self._y]):
                return True
            elif all([self._y != self._x, self._x, self._y]):
                return False
            if not node_queue:
                break
            depth += 1
        return False

    def layer_traverse(self, nodes: list, depth, x, y):
        queue = []
        for node in nodes:
            if node.val == x:
                self._x = depth
            if node.val == y:
                self._y = depth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return queue


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
