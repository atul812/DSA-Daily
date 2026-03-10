class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        if num >= 10:
            num = self.addDigits(self.numb(num))
        return num

       
    def numb(self, num):
        sumation = 0
        rem = num % 10
        quo = num // 10
        sumation = rem + quo
        return sumation
