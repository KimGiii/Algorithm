class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int):
        # 종료 조건 : 더이상 땅이 아닌 경우
        if i < 0 or i >= len(grid) or \
           j < 0 or j >= len(grid[0]) or \
           grid[i][j] != '1':
           return 

        grid[i][j] = 0

        # 실행 조건: 상하좌우 모두 탐색
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

    def numIslands(self, grid: List[List[str]]) -> int:
        # 예외 처리
        if not grid:
            return 0
        
        cnt = 0
        # 입력된 grid 탐색 시작
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    # 모든 육지 탐색 후 카운트 1 증가
                    cnt += 1

        return cnt