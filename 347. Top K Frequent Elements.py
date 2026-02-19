from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = defaultdict(int)

        for i in nums:
            dicti[i] += 1

        sorteditems = sorted(dicti.items(), key= lambda x: x[1], reverse = True)

        return [item[0] for item in sorteditems[:k]]
           
