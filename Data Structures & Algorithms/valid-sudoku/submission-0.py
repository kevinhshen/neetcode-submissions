class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        subBoxes=[[] for a in range(9)]
        for row in range(len(board)):

            numsRow=[]
            numsCol=[]
            
            # [][][]
            #  [][][]
            #  [][][]

            for col in range(len(board)):

                # check row
                if board[row][col] in numsRow and board[row][col] != '.':
                    return False
                else:
                    numsRow.append(board[row][col])

                # check column
                if board[col][row] in numsCol and board[col][row] != '.':
                    return False
                else:
                    numsCol.append(board[col][row])

                # check grid
                # row//3 == 0,1,2
                # col//3 == 0,1,2

                subBoxRow = row//3
                subBoxCol = col//3

                subBoxIndex = subBoxCol*3 + subBoxRow

                if board[row][col] in subBoxes[subBoxIndex] and board[row][col] != '.':

                    return False
                else:
                    subBoxes[subBoxIndex].append(board[row][col])

        return True

                
