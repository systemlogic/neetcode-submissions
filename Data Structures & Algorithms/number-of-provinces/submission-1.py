class Solution:

    def dfs(self, i, j, visited, isConnected):
        neighbor = [[]]


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        _dict = {}
        _row = len(isConnected)
        _col = len(isConnected[0]) 
        for row in range(_row):
            for col in range(_col):
                if isConnected[row][col]:
                    if row not in _dict:
                        _dict[row] = []
                    _dict[row].append(col)
        
        visit = []
        self.visited = set()
        self.count = 0
        print(_dict)
        def dfs(item):
            if item not in self.visited:
                self.visited.add(item)
            for list_item in _dict[item]:
                if list_item not in self.visited:
                    dfs(list_item)
        for item in range(_row):
            if item not in self.visited:
                self.count += 1
                dfs(item)
        return self.count





