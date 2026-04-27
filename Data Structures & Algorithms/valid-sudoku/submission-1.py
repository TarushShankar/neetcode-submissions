class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validating Row

        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        

        # Validating Column
        for j in range(9):
            s = set()
            for i in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        
        # Validating Box

        starts = [
            (0,0),(0,3),(0,6),
            (3,0),(3,3),(3,6),
            (6,0),(6,3),(6,6)
        ]

        for i, j in starts:
            s = set()
            for row in range(i,i+3):
                for column in range(j,j+3):
                    item = board[row][column]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)

        return True