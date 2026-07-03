class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def existRec(r, c, wordIndex):
            if wordIndex == len(word):
                return True
            if r < 0 or c < 0 or r>= ROWS or c >= COLS or word[wordIndex] != board[r][c] or board [r][c] == '#':
                return False
            
            #mark current spot as used
            board[r][c] = '#'

            #backtrack
            answer = existRec(r+1, c, wordIndex+1) or existRec(r-1, c, wordIndex+1) or existRec(r, c+1, wordIndex+1) or existRec(r, c-1, wordIndex+1)

            #set back to original (can do word[i] since only explore valid paths)
            board[r][c] = word[wordIndex]
            return answer

        #code to start from each avaialble letter
        for r in range(ROWS):
            for c in range(COLS):
                if existRec(r, c, 0):
                    return True
        return False
