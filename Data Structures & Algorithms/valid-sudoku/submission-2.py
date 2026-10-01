class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Have hashmap for each row, col, square
        # ex.: {row 1: set []}
        # Then, one iteration and put in each row, col, square
        # For square there are 8 so use formula r//3 x 3 + c//3 (this reasoning is tough)
        rows, cols = len(board), len(board[0])
        row_cnt = defaultdict(set)
        col_cnt = defaultdict(set)
        grids = defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row_cnt[r] or board[r][c] in col_cnt[c] or board[r][c] in grids[(r//3)*3 + (c//3)]:
                    return False
                row_cnt[r].add(board[r][c])
                col_cnt[c].add(board[r][c])
                grids[(r//3)*3 + (c//3)].add(board[r][c])
        return True




