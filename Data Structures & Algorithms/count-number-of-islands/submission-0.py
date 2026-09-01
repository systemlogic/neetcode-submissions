class Solution:

    def dfs(self, row, col, visited, grid):
        visited[row][col] == True
        grid[row][col] = "0"
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for neighbor_x, neighbor_y  in neighbors:
            new_x = neighbor_x + row
            new_y = neighbor_y + col
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and not visited[new_x][new_y] and grid[new_x][new_y] == "1":
                self.dfs(new_x, new_y, visited, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        count = 0
        for row in range(rows):
            for col in range(cols):
                if not visited[row][col] and grid[row][col] == "1":
                    count += 1
                    self.dfs(row, col, visited, grid)
        
        return count


        