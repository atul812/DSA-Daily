class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        ans = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            ans.append(arr1[i])
            i += 1
            ans.append(arr2[j])
            j += 1

        return ans
