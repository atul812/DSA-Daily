class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for list1 in matrix:
            i = 0
            j = len(list1)-1
            while(i<=j):
                mid = (i+j)//2
                if target == list1[mid]:
                    return True
                elif target < list1[mid]:
                    j = mid -1
                else:
                    i = mid + 1

        return False
