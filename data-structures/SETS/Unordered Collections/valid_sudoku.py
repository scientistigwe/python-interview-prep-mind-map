class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Step 1: Initialize sets to track seen numbers in rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Step 2: Iterate over each cell in the 9x9 Sudoku board
        for i in range(9):
            for j in range(9):
                num = board[i][j]

                # Skip empty cells
                if num == '.':
                    continue

                # Step 3: Check if the number is already in the current row
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # Step 4: Check if the number is already in the current column
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # Step 5: Calculate the index for the corresponding 3x3 sub-box
                box_index = (i // 3) * 3 + (j // 3)

                # Step 6: Check if the number is already in the current 3x3 sub-box
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)

        # If all checks pass, the board is valid
        return True


# Scenario Question:
# Sarah is a software developer working on a Sudoku validation tool. She needs to determine if a given Sudoku board configuration is valid according to Sudoku rules.
# A board is valid if each row, each column, and each of the nine 3x3 sub-boxes contain the digits 1-9 without repetition.

# Example 1: A valid Sudoku board
board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(Solution().isValidSudoku(board1))  # Output: True

# Follow-up Question 1:
# If Sarah changes the value in the first cell of the board to '8', what will the function return? Why?
# Answer: The function will return False because there will be two '8's in the first 3x3 sub-box (top-left corner), which violates the Sudoku rule.

# Example 2: An invalid Sudoku board
board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(Solution().isValidSudoku(board2))  # Output: False

# Follow-up Question 2:
# Sarah is testing the function with `board2`, and it returns False. Explain what caused the invalid result.
# Answer: The invalid result is caused by the presence of two '8's in the first 3x3 sub-box (top-left corner). According to Sudoku rules, a number cannot repeat in any 3x3 sub-box.

# Follow-up Question 3:
# Sarah is curious about how the function determines the sub-box index. How is the sub-box index calculated for any cell at position (i, j)?
# Answer: The sub-box index is calculated using the formula `(i // 3) * 3 + (j // 3)`. This formula maps each cell to its corresponding sub-box.
# For example, if the cell is at position (4, 7), the sub-box index is `(4 // 3) * 3 + (7 // 3)`, which equals `1 * 3 + 2 = 5`, corresponding to the middle-right sub-box.
