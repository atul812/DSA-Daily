# Selection sort O(n^2)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            minindex = i
            for j in range(i+1, n):
                if nums[j] < nums[minindex]:
                    minindex = j

            temp = nums[i]
            nums[i] = nums[minindex]
            nums[minindex] = temp

        return nums


# Bubble sort O(n^2)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums


# Insertion sort O(n^2)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            currval = nums[i]
            swapindex = i
            for j in range(i-1, -1, -1):
                if nums[j] > currval:
                    nums[j+1] = nums[j]
                    swapindex = j

            nums[swapindex] = currval

        return nums 
