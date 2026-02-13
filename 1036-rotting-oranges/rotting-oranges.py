class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # count number of oranges in cell
        # keep track of rotten oranges
        # all rotten oranges are start points

        n = len(grid)
        m = len(grid[0])
        freshOranges = 0
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    freshOranges += 1
                if grid[i][j] == 2:
                    q.append((0,i,j))
        

        seen = set()
        finalTime = 0
        while q:
            t, i, j = q.popleft()

            finalTime = max(finalTime,t)

            dir = [(1,0), (0,1), (-1,0), (0,-1)]

            for dx, dy in dir:
                nx = i +dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == 1 and (nx,ny) not in seen:
                        freshOranges -=1
                        seen.add((nx,ny))
                        q.append((t+1,nx,ny))
        # reachable oranges != oranges
        if freshOranges != 0:
            return -1
        return finalTime