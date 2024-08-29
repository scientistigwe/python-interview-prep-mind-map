# Scenario:
#
# Imagine you're a jewelry store owner who has a collection of various types of stones. Each stone in your inventory has a specific type, represented by a character in the string stones. Your store has a special collection of stones that are considered "jewels," and these are represented by a string jewels. You want to determine how many of your stones are part of this special collection of jewels.
#
# Problem Statement
# You're given two strings:
#
# jewels: A string where each character represents a type of stone that is considered a jewel. Each character in jewels is unique.
# stones: A string where each character represents a type of stone you have in your inventory.
# Write a function to determine how many stones in your inventory are also jewels.

# Function Signature:
#
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         pass
# Input:
#
# jewels (string): A string representing the types of stones that are jewels.
# stones (string): A string representing the types of stones you have.
# Output:
#
# An integer representing the number of stones that are also jewels.
# Constraints:
#
# 1
# ≤
# jewels.length
# ,
# stones.length
# ≤
# 50
# 1≤jewels.length,stones.length≤50
# jewels and stones consist of only English letters.
# All characters in jewels are unique.
# Example 1:
# Input:
#
# jewels = "aA"
# stones = "aAAbbbb"
# Output:
# Explanation:
# Jewels are 'a' and 'A'.
# Stones are 'aAAbbbb'.
# Stones 'a', 'A', and 'A' are jewels. The total count of these stones is 3.
# Example 2:
# Input:
# jewels = "z"
# stones = "ZZ"
# Output:
#
# Explanation:
#
# Jewels are 'z'.
# Stones are 'ZZ'.
# No stones match the jewel type 'z'. Therefore, the count is 0.
#
# Add-On Questions and Answers
# What is the time complexity of the numJewelsInStones function?
#
# Answer: The time complexity of the numJewelsInStones function is O(n), where 𝑛 is the length of the stones string.# This is because the function iterates over each stone once and performs a constant-time lookup in the jewel_set for each stone.
#
# What is the space complexity of the numJewelsInStones function?
# Answer: The space complexity of the numJewelsInStones function is  O(m), where  m is the length of the jewels string. This is because the jewel_set stores the unique characters from the jewels string, which takes up space proportional to the number of unique jewels.
#
# How would you modify the solution if the jewels string could contain duplicate characters?
# Answer: If the jewels string could contain duplicate characters, you would need to modify the solution to handle this. The updated approach would involve counting the occurrences of each jewel in the jewels string and then checking how many of those occurrences are present in the stones string. Here’s a modified version of the solution:
# Solution Implementation
from collections import Counter

from pythonClass import jewel_counter, jewels, stones


class Soluton:
    def jewels_and_stones(self, jewels:str, stones:str) -> int:
        jewel_set = set(jewels)
        num_stones = 0
        print(Counter(jewels))
        for char in stones:
            if char in jewel_set:
                num_stones += 1

        return num_stones
solution = Soluton()
x = 'abBBab'
y = 'babacda'
print(solution.jewels_and_stones(x, y))


# Approach 2: using counter
def jewels_and_stones_counter(jewels:str, stones:str) -> int:
    stone_set = set(stones)
    jewel_counter = Counter(jewels)
    num_stones = 0
    print(jewel_counter)
    for char in stone_set:
        if char in jewel_counter:
            num_stones += jewel_counter[char]
    return(num_stones)

x = 'abBBab'
y = 'babacda'
print(jewels_and_stones_counter(jewels=y, stones=x))