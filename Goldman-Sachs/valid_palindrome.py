# Scenario: Input Validation for a Content Moderation System (125. Valid Palindrome)
#
# Imagine you are developing a content moderation system for a social media platform.
# One of the features the system requires is the ability to detect palindromes within user-generated content.
# A palindrome is a sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and case.
# The platform wants to identify whether certain strings (such as usernames, titles, or messages) are palindromes,
# as palindromic sequences are often used for creative effects or spam.
#
# The system needs to handle various types of input, including those with special characters and mixed cases.
# Your task is to write a function that checks if a given string is a valid palindrome by only considering
# alphanumeric characters and ignoring case.
#
# Example Usage:
# - Input: "A man, a plan, a canal: Panama"
#   Output: True
#   Explanation: After removing non-alphanumeric characters and converting to lowercase,
#   the string becomes "amanaplanacanalpanama", which is a palindrome.
#
# - Input: "race a car"
#   Output: False
#   Explanation: After processing, the string becomes "raceacar", which is not a palindrome.
#
# Complexity Analysis:
# - Time Complexity: O(n), where n is the length of the string.
#   - The string is processed in a single pass to filter and convert characters,
#     and another pass is used to check if it reads the same forwards and backwards.
# - Space Complexity: O(n), where n is the number of alphanumeric characters in the string.
#   - The space is used to store the cleansed list of characters.
#
# Follow-up Questions:
# - What if the input string is extremely large? How would you handle performance?
#   - Answer: If the input string is very large, you could optimize the space usage by using two pointers
#     to check for palindrome properties directly, without creating an additional list.
#
# - How would you modify the function to check for palindromes in real-time as characters are typed?
#   - Answer: To check in real-time, you could use a deque (double-ended queue) to dynamically manage
#     characters from both ends of the string as it is being built, allowing immediate palindrome checks
#     with each new character typed.
#
# - Can the solution handle Unicode characters, such as accented letters?
#   - Answer: The current solution only handles ASCII alphanumeric characters. To handle Unicode,
#     you would need to adjust the `isalnum()` method to correctly identify alphanumeric characters
#     in different scripts and apply normalization (e.g., `NFKD`) to handle accented characters.
#

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # List comprehension to create a cleansed list of alphanumeric characters in lowercase
        cleansed_s = [char.lower() for char in s if char.isalnum()]

        # Check if the cleansed list is equal to its reverse
        return cleansed_s == cleansed_s[::-1]


# Example usage:
solution = Solution()
s = "A man, a plan, a canal: Panama"
print(solution.validPalindrome(s))  # Output: True

s2 = "race a car"
print(solution.validPalindrome(s2))  # Output: False
