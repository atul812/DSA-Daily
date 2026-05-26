class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window_size = sum(nums[:k])
        max_sum = window_size

        for i in range(k, len(nums)):
            window_size += nums[i]
            window_size -= nums[i-k]
            max_sum = max(max_sum, window_size)

        return max_sum/k
        
