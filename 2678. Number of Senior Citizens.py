class Solution:
    def countSeniors(self, arr: List[str]) -> int:
        count = 0
        for i in range(len(arr)):
            age = int(arr[i][11:13])
            if age > 60:
                count+= 1

        return count
