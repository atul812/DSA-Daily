sliding window approach (will not work for bigger test cases due to O(N*K))
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        if k >= len(nums):
            return [max(nums)]
        for i in range(len(nums)):
            window_size = nums[i:k]
            max_now = max(window_size)
            ans.append(max_now)
            if k == len(nums)-1:
                i += 1
                window_size = nums[i:k+1]
                max_now = max(window_size)
                ans.append(max_now)
                break
            k += 1
        return ans
            

efficient (sliding window + deque):
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        left = 0

        for right in range(len(nums)):

            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            if q[0] < left:
                q.popleft()

            if right + 1 >= k:
                res.append(nums[q[0]])
                left += 1
        return res
            
