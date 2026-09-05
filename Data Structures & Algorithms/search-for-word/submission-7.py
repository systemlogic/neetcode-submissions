class Solution:

    def dfs(self, row, col, board, word, visited, new_word = ""):

        # This condition make sure only progressive match
        if not word.startswith(new_word):
            return

        new_word += board[row][col]
        visited[row][col] = True

        if len(new_word) == len(word): 
            if word == new_word:
                return True

        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for n_x, n_y in neighbors:
            new_x = n_x + row
            new_y = n_y + col
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and not visited[new_x][new_y] :
                if self.dfs(new_x, new_y, board, word, visited, new_word):
                    return True
        new_word = new_word[:-1]
        visited[row][col] = False        
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                visited = [[False for _ in range(cols)] for _ in range(rows)]
                # word.startswith(board[row][col]) in below line will help if first char in search word is on
                # on the grid.
                if word.startswith(board[row][col]) and self.dfs(row, col, board, word, visited): 
                    return True
        return False
