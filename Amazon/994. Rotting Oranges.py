class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >=m or nc >= n or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
            
            time += 1
        return time if fresh == 0 else -1