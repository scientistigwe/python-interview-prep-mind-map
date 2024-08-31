# Scenario: Content Quality Check for a Typing Practice Website
# (Leetcode equivalent: Is pangram - #1832)
# Imagine you are a developer for a website that helps people practice typing.
# The website has a feature where users type sentences that contain every letter of the alphabet (i.e., pangrams).
# You need to implement a function that checks whether a given sentence meets this criterion.

# Problem Statement:
# Given a string sentence containing only lowercase English letters,
# return True if the sentence is a pangram, or False otherwise.

# Example Usage:
# Example 1:
# Input: "thequickbrownfoxjumpsoverthelazydog"
# Output: True
# Explanation: This sentence contains all letters from 'a' to 'z'.

# Example 2:
# Input: "leetcode"
# Output: False
# Explanation: This sentence does not contain all the letters of the alphabet.

# Constraints:
# The sentence's length is between 1 and 1000 characters.
# The sentence consists only of lowercase English letters.

# Implementation:
# Now, let's implement the solution:

class SentenceValidator:
    # Constructor to initialize the sentence
    def __init__(self, sentence: str):
        self.sentence = sentence

    # Method to check if the sentence is a pangram
    def checkIfPangram(self) -> bool:
        # The set of all lowercase English letters
        alphabet = set("abcdefghijklmnopqrstuvwxyz")

        # Convert the sentence to a set to find unique characters
        sentence_set = set(self.sentence)

        # Check if all the letters in the alphabet are in the sentence
        is_pangram = alphabet.issubset(sentence_set)

        # Return True if the sentence is a pangram, False otherwise
        return is_pangram


# Example Usage
# 1. Creating an instance of SentenceValidator for a known pangram
validator1 = SentenceValidator("thequickbrownfoxjumpsoverthelazydog")
print(validator1.checkIfPangram())  # Output: True

# 2. Creating an instance of SentenceValidator for a non-pangram
validator2 = SentenceValidator("leetcode")
print(validator2.checkIfPangram())  # Output: False
