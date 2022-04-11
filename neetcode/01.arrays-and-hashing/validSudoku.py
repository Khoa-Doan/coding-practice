class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        
        # Initialize 2D-array
        grids = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                grids[i][j] = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows[r] or val in cols[c] or val in grids[r//3][c//3]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                grids[r//3][c//3].add(val)
        return True