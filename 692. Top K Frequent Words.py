class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            if i not in d: d[i] = 1
            else: d[i] += 1
        
        # d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        # return [i[0] for i in d[:k]]

        heap = [(-freq, word) for word, freq in d.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for i in range(k)] 