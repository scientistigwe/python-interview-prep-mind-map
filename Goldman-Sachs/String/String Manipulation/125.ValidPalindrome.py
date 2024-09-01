# Interview Scenario:
#
# Context: Imagine you are working as a software engineer at a tech company that specializes in developing advanced text processing applications. Your team is currently working on a feature for a text analysis tool that will help users identify and clean up palindromes from their input text. Palindromes are strings that read the same forwards and backwards, ignoring spaces, punctuation, and letter case.
#
# Interview Question:
#
# Problem Statement:
#
# You are tasked with implementing a function that checks whether a given string is a valid palindrome. For this problem, a valid palindrome is defined as a string that reads the same backward as forward when considering only alphanumeric characters and ignoring letter case.
#
# Requirements:
#
# Function Signature:
#
# python
# Copy code
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         pass
# Input:
#
# A single string s (1 ≤ |s| ≤ 2 * 10^5) that consists of printable ASCII characters.
# Output:
#
# Return True if the given string is a valid palindrome, otherwise return False.
# Example:
#
# Input: "A man, a plan, a canal: Panama"
#
# Output: True
#
# Input: "race a car"
#
# Output: False
#
# Explanation:
#
# The function should only consider alphanumeric characters (letters and digits) and ignore all other characters (spaces, punctuation).
# It should also be case insensitive, meaning 'A' and 'a' are treated as the same character.
# Example Test Cases:
#
# python
# Copy code
# sol = Solution()
#
# # Test case 1: Simple case with mixed case and punctuation
# print(sol.validPalindrome("A man, a plan, a canal: Panama"))  # Expected output: True
#
# # Test case 2: Case with non-palindromic structure
# print(sol.validPalindrome("race a car"))  # Expected output: False
#
# # Test case 3: Only one character
# print(sol.validPalindrome("a"))  # Expected output: True
#
# # Test case 4: Empty string
# print(sol.validPalindrome(""))  # Expected output: True
#
# # Test case 5: String with only non-alphanumeric characters
# print(sol.validPalindrome(".,?!"))  # Expected output: True
# Instructions:
#
# Implementation Details:
#
# Cleanse the input string by removing non-alphanumeric characters and converting all letters to lowercase.
# Compare the cleansed string with its reverse to determine if it is a palindrome.
# Optimization Notes:
#
# Ensure the solution is efficient and handles the upper limit of input size effectively.
# Constraints:
#
# Do not use external libraries or dependencies.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        cleansed_s = [char.lower() for char in s if char.isalnum()]
        return cleansed_s == cleansed_s[::-1]

sol = Solution()
print(sol.validPalindrome("A man, a plan, a canal: Panama"))