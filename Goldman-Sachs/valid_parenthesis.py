# Scenario: Validation of Parentheses in Code Editors (Leetcode: 20. Valid Parentheses)
#
# Imagine you're developing a code editor that helps developers by automatically checking the validity of parentheses
# as they type. This feature ensures that every opening parenthesis has a corresponding closing parenthesis and that
# they are correctly nested. Your task is to implement a function that checks whether a string containing parentheses,
# brackets, and braces is valid.
#
# Example Usage:
# - Input: "()"
#   Output: True
#   Explanation: The string contains one pair of valid parentheses.
#
# - Input: "([{}])"
#   Output: True
#   Explanation: The string contains correctly nested parentheses, brackets, and braces.
#
# - Input: "(]"
#   Output: False
#   Explanation: The string contains mismatched parentheses.
#
# Complexity Analysis:
# - Time Complexity: O(n), where n is the length of the string. Each character is processed exactly once.
# - Space Complexity: O(n) in the worst case, where n is the length of the string (if all characters are opening parentheses).

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_parenthesis = {")": "(", "}": "{", "]": "["}

        for char in s:
            # If the character is a closing parenthesis
            if char in valid_parenthesis:
                # Check if the stack is not empty and if the top element matches the expected opening parenthesis
                if stack and stack[-1] == valid_parenthesis[char]:
                    stack.pop()  # Remove the matching opening parenthesis from the stack
                else:
                    return False  # If there's no match, the string is invalid
            else:
                # If it's an opening parenthesis, push it onto the stack
                stack.append(char)

        # If the stack is empty, all parentheses were matched; otherwise, it's invalid
        return not stack


# Example usage:
solution = Solution()
print(solution.isValid("()"))  # Output: True
print(solution.isValid("([{}])"))  # Output: True
print(solution.isValid("(]"))  # Output: False
