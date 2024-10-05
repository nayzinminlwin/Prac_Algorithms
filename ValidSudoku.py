from typing import List


class Solution:
    def Valid_Sudoku(self, board: List[List[str]])->bool:
        status = True
        colArr = []
        boxArr = []
        for rowNum in range(len(board)):
            
            for itemsIndex in range(len(board[rowNum])):
                if board[rowNum][itemsIndex] == "." or 0<int(board[rowNum][itemsIndex])<10:
                    if board[rowNum][itemsIndex] == ".":
                        board[rowNum][itemsIndex] = 0
                    else:
                        board[rowNum][itemsIndex] = int(board[rowNum][itemsIndex])

                    # boxArr.append(board[rowNum][itemsIndex])
                else:
                    status = False
                    print("ret")
                    return status
                
            if sol.gotDuplicate(board[rowNum]):
                status = False
                print("gotta return row false by funtion")
                return status

            colArr.append(board[rowNum][0])

        if sol.gotDuplicate(colArr):
            status = False
            print("gotta return col false by funtion")
            return status


        print("column arrary : ",colArr)
        # print("Box array : ",boxArr)
            
        print(board)

        return status
    
    def gotDuplicate(self,nums:List[int])->bool:
        found = set()
        for j in nums:
            if j in found and j!=0 :
                return True
            else:
                found.add(j)
                
        return False


sol = Solution()
print(sol.Valid_Sudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))