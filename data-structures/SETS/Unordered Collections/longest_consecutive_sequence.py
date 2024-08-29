# Scenario Script with Answers

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# Scenario:
# You are a software engineer at a tech company that specializes in developing high-performance 
# data processing systems. Your team has been assigned a critical task for an upcoming product release: 
# to optimize a feature that analyzes large datasets of user activity logs. One specific requirement is to identify 
# the longest sequence of consecutive days on which a user was active.

# For example, given a list of days on which a user logged into the system, the goal is to determine the longest streak 
# of consecutive active days. The datasets are huge, containing millions of entries, and the solution must be efficient, 
# operating within O(n) time complexity.

# Your teammate has proposed the following code as a solution:

solution = Solution()

# Example input
input_data = [100, 4, 200, 1, 3, 2]

# Answer to Question 1: Understanding the Code
# The code works by first converting the input list of numbers into a set, which allows for O(1) time complexity when 
# checking for the presence of elements. It then iterates through the set, checking if each number is the start of a 
# potential sequence (i.e., num - 1 is not in the set). If it is the start of a sequence, it counts the length of 
# that sequence by incrementing the number and checking for the next consecutive number in the set. The maximum length 
# found during this process is stored and returned as the result. The approach is efficient because each number is processed 
# only once, leading to an O(n) time complexity.

# Example of code execution
output = solution.longestConsecutive(input_data)
print("Output for input [100, 4, 200, 1, 3, 2]:", output)  # Expected Output: 4

# Answer to Question 2: Scenario Application
# For the dataset [1, 2, 3, 10, 11, 12, 13], the code will start by identifying 1 as the start of the sequence [1, 2, 3], 
# resulting in a current streak of 3. Next, it will identify 10 as the start of the sequence [10, 11, 12, 13], resulting 
# in a current streak of 4. The code will then compare the two streaks and return 4 as the longest streak.

# Example of code execution with different input
input_data = [1, 2, 3, 10, 11, 12, 13]
output = solution.longestConsecutive(input_data)
print("Output for input [1, 2, 3, 10, 11, 12, 13]:", output)  # Expected Output: 4

# Answer to Question 3: Optimization Consideration
# Memory concerns could arise when working with extremely large datasets because the set data structure requires O(n) space. 
# To mitigate memory usage, you might consider alternative data structures or processing techniques that reduce memory footprint, 
# such as processing data in chunks or using a more memory-efficient method like sorting (although sorting would increase time 
# complexity to O(n log n)).

# Answer to Question 4: Edge Cases
# If the input list is empty, the code returns 0, which is the correct behavior since there are no elements to form a sequence.
# If all numbers in the list are the same (e.g., [7, 7, 7, 7]), the code will identify that there is no sequence of consecutive 
# numbers and return a streak length of 1. This is also correct since the longest "sequence" in this context is just the number 
# itself appearing once.

# Edge case examples
output = solution.longestConsecutive([])  # Expected Output: 0
print("Output for empty input []:", output)

output = solution.longestConsecutive([7, 7, 7, 7])  # Expected Output: 1
print("Output for input [7, 7, 7, 7]:", output)

# Answer to Question 5: Real-World Application
# If the requirement changes to find the longest sequence of consecutive active hours in a day instead of days in a year, 
# you would need to modify the input data to represent hours instead of days. The code logic would largely remain the same, 
# but you'd apply it to a dataset where each element represents an hour of activity (e.g., hours could be represented by integers 
# from 0 to 23). The set would still be used to track hours, and the same process of identifying sequences would apply.

# Real-world scenario application
input_data_hours = [0, 1, 2, 4, 5, 6, 23]
output = solution.longestConsecutive(input_data_hours)
print("Output for input hours [0, 1, 2, 4, 5, 6, 23]:", output)  # Expected Output: 3
