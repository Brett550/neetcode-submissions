class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check cols
        nums = set()
        for col in range(9):
            nums.clear()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in nums:
                    return False
                nums.add(board[i][col])

        nums.clear()
        #check rows
        for row in range(len(board)):
            nums.clear()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in nums:
                    return False
                nums.add(board[row][i])

        nums.clear()
        #check each box
        for square in range(9):
            nums.clear()
            for r in range(3):
                for c in range(3):
                    row = (square//3)*3 + r
                    col = (square%3)*3 + c
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in nums:
                        return False
                    nums.add(board[row][col])
        return True
