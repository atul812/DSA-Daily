class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max(nums[n-1]*nums[n-2]*nums[n-3], nums[0]*nums[1]*nums[n-1])

  # after sorting the array, we simply compute both possibilities which is nums[-1] * nums[-2] * nums[-3] and nums[0] * nums[1] * nums[-1], and return the maximum of the two.
