# Scenario: Academic Performance Tracking System (LeetCode: #1086. High Five)
# 
# Imagine you are working as a software engineer for an online education platform. 
# The platform tracks student scores across multiple assessments. Each student 
# can have multiple scores, and your task is to compute the average of their top five scores.
# 
# The goal is to write a function that processes a list of scores for multiple students, 
# identifies the top five scores for each student, and calculates the average of those top five scores. 
# The average should be an integer, and the final result should include each student's ID 
# and their respective top five average, sorted by student ID.
#
# Problem Statement:
# Given a list of scores where each score is represented as [student_id, score], 
# compute each student's top five average scores. Return the result as a list of 
# pairs [student_id, topFiveAverage], sorted by student ID.
#
# Example:
# Input: items = [[1, 92], [1, 91], [2, 93], [2, 97], [1, 60], [2, 77], 
#                 [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
# Output: [[1, 87], [2, 88]]
#
# Explanation:
# - Student 1 has scores: [92, 91, 60, 65, 87, 100]. Top five scores: [100, 92, 91, 87, 65]. 
#   Their average is (100 + 92 + 91 + 87 + 65) // 5 = 87.
# - Student 2 has scores: [93, 97, 77, 100, 76]. Top five scores: [100, 97, 93, 77, 76]. 
#   Their average is (100 + 97 + 93 + 77 + 76) // 5 = 88.
#
# Complexity Analysis:
# - Time Complexity: O(n log 5) = O(n), where n is the number of scores.
#   - We use a min-heap to maintain the top 5 scores for each student. 
#   - Insertion into the heap and removal of the smallest element both take O(log 5) time, 
#     which simplifies to O(1) since the heap size is fixed at 5.
#   - Sorting the student IDs at the end takes O(m log m), where m is the number of students.
# - Space Complexity: O(m), where m is the number of students.
#   - We use a dictionary to store the heap of top 5 scores for each student.
# 
# Follow-up Questions:
# - How would you modify the solution if the top 3 scores are required instead of the top 5?
#   - Answer: To adjust the solution to consider the top 3 scores instead of the top 5, you would 
#     simply change the heap size limit from 5 to 3. Specifically, replace the condition 
#     `if len(score_dict[student_id]) > 5:` with `if len(score_dict[student_id]) > 3:`. The rest 
#     of the logic remains the same, as the heap operations will still ensure that only the top 
#     3 scores are kept in the heap for each student.
#
# - How would you handle the case where a student has fewer than 5 scores?
#   - Answer: If a student has fewer than 5 scores, the solution will still work correctly. The 
#     heap will simply contain all of the available scores for that student. When calculating the 
#     average, you should divide by the actual number of scores in the heap, not necessarily by 5. 
#     This would require changing `sum(score_dict[student_id]) // 5` to 
#     `sum(score_dict[student_id]) // len(score_dict[student_id])`.
#
# - Can you optimize the solution if the number of students or the number of scores is extremely large?
#   - Answer: For an extremely large number of students or scores, you could consider the following optimizations:
#     1. Use a more space-efficient data structure to manage the scores, such as a priority queue 
#        that can handle streaming data in real time.
#     2. Process scores in batches to reduce memory usage and possibly use external storage or 
#        databases if the data set is too large to fit in memory.
#     3. Parallelize the processing of student scores to take advantage of multi-core processors 
#        if the operation is CPU-bound.
#
# - What if the scores are in a streaming fashion (one score at a time)? How would you modify the solution to handle this?
#   - Answer: If scores are provided in a streaming fashion, you would need to process each score as 
#     it arrives. The current solution is already well-suited for streaming data because it maintains 
#     a running min-heap for each student. You can simply apply the same heap operations (`heappush` 
#     and `heappop`) as each new score is received, ensuring that the heap never exceeds 5 elements. 
#     At any point, you can compute the top five average for any student based on the current state of 
#     their heap.
#

from collections import defaultdict
import heapq

class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        # Use a dictionary to map each student ID to a min-heap (to keep the top 5 scores)
        score_dict = defaultdict(list)
        result = []

        # Iterate over each student ID and score in the input list
        for student_id, score in items:
            # Push the score onto the student's heap
            heapq.heappush(score_dict[student_id], score)

            # If the heap exceeds 5 scores, remove the smallest score (maintain top 5)
            if len(score_dict[student_id]) > 5:
                heapq.heappop(score_dict[student_id])

        # Sort the student IDs and calculate the top five average for each student
        for student_id in sorted(score_dict.keys()):
            top_five_average = sum(score_dict[student_id]) // 5  # Integer division
            result.append([student_id, top_five_average])

        return result

# Example usage:
solution = Solution()
items = [[1, 92], [1, 91], [2, 93], [2, 97], [1, 60], [2, 77], 
         [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(solution.highFive(items))  # Output: [[1, 87], [2, 88]]
