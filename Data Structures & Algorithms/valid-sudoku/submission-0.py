from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        hm = defaultdict(set)
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                currSubBox = (row // 3, col // 3)

                if board[row][col].isnumeric():
                
                    if board[row][col] in hm[("row", row)] or board[row][col] in hm[("col", col)] or board[row][col] in hm[("subbox", currSubBox)]:
                        return False
                    else:
                        hm[("row", row)].add(board[row][col])
                        hm[("col", col)].add(board[row][col])
                        hm[("subbox", currSubBox)].add(board[row][col])
            

        return True
