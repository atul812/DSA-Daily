from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        freq = Counter(words[0])
        for word in words[1:]:
            freq &= Counter(word)

        for ch in freq:
            ans.extend([ch] * freq[ch])

        return ans
