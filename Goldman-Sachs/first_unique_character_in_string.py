# Scenario: User Input Validation for Unique Identifiers (387. First Unique Character in a String)
#
# Imagine you're working on a software system where users input strings as unique identifiers for items.
# The system needs to find the first unique character in the string, which could be used to generate a short code 
# or handle other operations. Your task is to implement a function that identifies the first unique character 
# in the string and returns its index. If there is no unique character, the function should return -1.
#
# Example Usage:
# - Input: "leetcode"
#   Output: 0 (The first unique character is 'l', at index 0)
#
# - Input: "loveleetcode"
#   Output: 2 (The first unique character is 'v', at index 2)
#
# - Input: "aabb"
#   Output: -1 (There is no unique character)
#
# Complexity Analysis:
# - Time Complexity: O(n), where n is the length of the string.
#   - We make a single pass to count characters and another to find the first unique one.
# - Space Complexity: O(1), because the space required for the character count is fixed (26 letters in the alphabet).
#
# Follow-up Questions:
# - What if the string is very long? Would your solution be efficient?
#   - Answer: The solution is efficient with O(n) time complexity, which is optimal for this problem.
#
# - How would you handle case sensitivity or special characters?
#   - Answer: You could normalize the string (e.g., convert to lowercase) before processing, and include logic 
#     to handle special characters depending on the requirements.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Dictionary to store the frequency of each character
        char_count = {}

        # First pass: count the frequency of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Second pass: find the first character with a count of 1
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        # If no unique character is found, return -1
        return -1


# Example usage:
solution = Solution()
s1 = "leetcode"
print(solution.firstUniqChar(s1))  # Output: 0

s2 = "loveleetcode"
print(solution.firstUniqChar(s2))  # Output: 2

s3 = "aabb"
print(solution.firstUniqChar(s3))  # Output: -1
