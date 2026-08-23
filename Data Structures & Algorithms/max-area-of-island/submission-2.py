class Solution:
    def dfs(self, x, y, visited, grid):
        visited[x][y] = 1
        visit = [[x,y]]
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        area = 1
        while visit:
            tmp = []
            while visit:
                row, col = visit.pop(0)
                for n_x, n_y in neighbors:
                    new_x = n_x + row
                    new_y = n_y + col
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and not visited[new_x][new_y] and grid[new_x][new_y]:
                        visited[new_x][new_y] = True
                        area += 1
                        tmp.append([new_x, new_y])
            visit[:] = tmp
        return area                        



    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        self.max_area = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col]:
                    area = self.dfs(row, col, visited, grid)
                    self.max_area = max(self.max_area, area)

        return self.max_area