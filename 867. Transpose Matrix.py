class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for row in zip(*matrix):
            ans += [list(row)]

        return ans

       
