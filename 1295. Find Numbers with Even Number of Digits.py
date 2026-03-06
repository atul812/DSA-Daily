class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            count = 0
            string = str(nums[i])
            for c in string:
                count += 1

            if count % 2 == 0:
                ans += 1

        return ans
