class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        set_a = set()
        set_b = set()
        both = set()
        result = []
        for i in range(n):
            set_a.add(A[i])
            set_b.add(B[i])
            if A[i] in set_b: both.add(A[i])
            if B[i] in set_a: both.add(B[i])

            result.append(len(both))
        return result
