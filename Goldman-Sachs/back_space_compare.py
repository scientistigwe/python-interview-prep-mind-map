class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Scenario: Comparing Text After Backspacing in a Text Editor
        #
        # Imagine you are developing a text editor that supports text input with backspace operations.
        # You want to implement a feature to compare two strings after all backspaces have been applied.
        # Each '#' character represents a backspace that deletes the previous character.
        # The task is to determine if the final versions of both strings are the same after processing backspaces.
        #
        # Example Usage:
        # - Input: s = "ab#c", t = "ad#c"
        #   Output: True
        #   Explanation: Both strings become "ac" after applying backspaces.
        #
        # - Input: s = "ab##", t = "c#d#"
        #   Output: True
        #   Explanation: Both strings become "" (empty) after applying backspaces.
        #
        # - Input: s = "a#c", t = "b"
        #   Output: False
        #   Explanation: After backspacing, s becomes "c" while t remains "b".

        def get_next_valid_char_index(index: int, string: str) -> int:
            # Helper function to find the next valid character index considering backspaces.
            # It moves the index left while handling backspace operations.
            backspace_count = 0
            while index >= 0:
                if string[index] == '#':
                    backspace_count += 1
                elif backspace_count > 0:
                    backspace_count -= 1
                else:
                    break
                index -= 1
            return index

        i, j = len(s) - 1, len(t) - 1

        # Compare the final forms of both strings after processing backspaces
        while i >= 0 or j >= 0:
            i = get_next_valid_char_index(i, s)
            j = get_next_valid_char_index(j, t)

            # Compare characters if both indices are valid
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:  # One string is exhausted while the other is not
                return False

            i -= 1
            j -= 1

        return True

# Example usage:
solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c"))  # Output: True
print(solution.backspaceCompare("ab##", "c#d#"))  # Output: True
print(solution.backspaceCompare("a#c", "b"))  # Output: False
