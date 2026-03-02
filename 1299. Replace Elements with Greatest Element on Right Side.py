class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxsofar = -1

        for i in range(len(arr)-1, -1, -1):
            current = arr[i]
            arr[i] = maxsofar
            maxsofar = max(maxsofar, current)

        return arr
