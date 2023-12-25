# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Definition for a binary tree node.
        hashmap={}
        def bfs(root):
            queue=[]
            queue.append(root)
            while queue:
                r=queue.pop(0)
                if r.left and r.left.val not in hashmap:
                    queue.append(r.left)
                    hashmap[r.left.val]=r
                if r.right and r.right.val not in hashmap:
                    queue.append(r.right)
                    hashmap[r.right.val]=r
        bfs(root)
        result=[]
        while (p.val!=root.val):
            result.append(p.val)
            p=hashmap[p.val]
        while q.val not in result and q.val in hashmap:
            q=hashmap[q.val]
        return q
            
  