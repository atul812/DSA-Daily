class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        expected_arr = list(range(1, n))+[n-1]

        return nums == expected_arr
