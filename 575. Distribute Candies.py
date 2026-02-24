class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        freq = defaultdict(int)

        for candy in candyType:
            freq[candy] += 1

        n = len(candyType)//2

        if len(freq.values()) > n:
            return n
        elif len(freq.values()) < n:
            return len(freq.values())
        else:
            return n
