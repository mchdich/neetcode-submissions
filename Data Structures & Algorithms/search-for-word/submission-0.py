class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    res = self.bt(board, word, 0, r, c)
                    if res:
                        return True
        return False
    def bt(self, board, word, i, r, c):
        if i == len(word):
            return True
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == "":
            return False
        if board[r][c] != word[i]:
            return False
        letter = board[r][c]
        board[r][c] = "" #necessary to mark
        if self.bt(board, word, i+1, r+1, c):
            return True
        if self.bt(board, word, i+1, r-1, c):
            return True
        if self.bt(board, word, i+1, r, c+1):
            return True
        if self.bt(board, word, i+1, r, c-1):
            return True
        board[r][c] = letter
        return False