# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque()
        d = {}
        q.append([root, 0, 0])
        while len(q) > 0:
            size = len(q)
            level_dict = {}
            for i in range(size):
                node, indi, level = q.popleft()
                if indi in level_dict:
                    level_dict[indi].append((node.val, level))
                else:
                    level_dict[indi] = [(node.val, level)]
                if node.left:
                    q.append([node.left, indi - 1, level + 1])
                if node.right:
                    q.append([node.right, indi + 1, level + 1])

            for indi in level_dict:
                level_dict[indi].sort(key=lambda x: (x[1], x[0]))
                if indi in d:
                    d[indi].extend([val for val, _ in level_dict[indi]])
                else:
                    d[indi] = [val for val, _ in level_dict[indi]]

        res = []
        for i in sorted(d):
            res.append(d[i])

        return res
