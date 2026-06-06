# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result=[]
        que=deque([root])
        while que:
            temp=[]
            qrange=len(que)
            for _ in range(qrange):
                e=que.popleft()
                temp.append(e.val)
                if e.left is not None:
                    que.append(e.left)
                if e.right is not None:
                    que.append(e.right)
            result.append(temp)
        return result
