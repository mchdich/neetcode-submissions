# Brute force O(n^2) O(1)
# Set O(n) O(n)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # deal with . logic
        n = len(board)
        for row in range(n):
            seen = set()
            for col in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        for col in range(n):
            seen = set()
            for row in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        x_idx, y_idx = 0, 0
        while y_idx < n:
            while x_idx < n:
                seen = set()
                for row in range(x_idx, x_idx + 3):
                    for col in range(y_idx, y_idx + 3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
                x_idx += 3
            x_idx = 0
            y_idx += 3    
        return True