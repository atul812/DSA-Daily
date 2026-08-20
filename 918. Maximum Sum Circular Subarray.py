class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        total_max, total_min = nums[0], nums[0]
        currmax, currmin = 0, 0

        for n in nums:
            total += n

            currmax = max(currmax, 0)
            currmax += n
            total_max = max(total_max, currmax)

            currmin = min(currmin, 0)
            currmin += n
            total_min = min(total_min, currmin)

        if total_max < 0:
            return total_max 

        return max(total_max, total - total_min)
