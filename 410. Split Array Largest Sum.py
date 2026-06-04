class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        for i in range(len(nums)):
            start = max(start, nums[i])
            end += nums[i]
        
        while start < end:
            mid = start + (end - start) // 2
            summ = 0
            piece = 1
            for num in nums:
                if summ + num > mid:
                    summ = num
                    piece += 1
                else:
                    summ += num
            
            if piece > k:
                start = mid + 1
            else:
                end = mid
        
        return start
