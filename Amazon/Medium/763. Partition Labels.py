class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ind = {}
        ans = []

        for i, j in enumerate(s):
            last_ind[j] = i
        
        size = 0
        end = 0
        for i, j in enumerate(s):
            size += 1
            end = max(end, last_ind[j])
            if i == end:
                ans.append(size)
                size = 0

        return ans