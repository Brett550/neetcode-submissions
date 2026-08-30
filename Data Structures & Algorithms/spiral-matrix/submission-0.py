class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        
        topRow = 0
        bottomRow = len(matrix)
        leftCol = 0
        rightCol = len(matrix[0])

        while topRow < bottomRow and leftCol < rightCol:
            #top col
            for i in range(leftCol, rightCol):
                answer.append(matrix[topRow][i])
            topRow +=1

            #right col (down)
            for i in range(topRow, bottomRow):
                answer.append(matrix[i][rightCol-1])
            rightCol -= 1

            #check conditions again
            if not (leftCol < rightCol and topRow < bottomRow):
                break


            #bottom row
            for i in range(rightCol-1, leftCol-1, -1):
                answer.append(matrix[bottomRow-1][i])
            bottomRow -= 1

            #left col (up)
            for i in range(bottomRow-1, topRow-1, -1):
                answer.append(matrix[i][leftCol])
            leftCol +=1
        return answer