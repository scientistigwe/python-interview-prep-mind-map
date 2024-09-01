import os

# Define the directory structure
categories = {
    "Arrays": [
        "1.TwoSum", "88.MergeSortedArray", "42.TrappingRainWater", "53.MaximumSubarray",
        "56.MergeIntervals", "15.3Sum", "33.SearchinRotatedSortedArray", "189.RotateArray",
        "79.WordSearch", "217.ContainsDuplicate", "268.MissingNumber", "560.SubarraySumEqualsK",
        "75.SortColors", "912.SortanArray", "38.CountandSay", "259.3SumSmaller", "347.TopKFrequentElements",
        "66.PlusOne", "118.Pascal'sTriangle", "119.Pascal'sTriangleII", "128.LongestConsecutiveSequence",
        "462.MinimumMovestoEqualArrayElementsII", "907.SumofSubarrayMinimums", "370.RangeAddition",
        "824.GoatLatin", "852.PeakIndexinaMountainArray", "628.MaximumProductofThreeNumbers",
        "152.MaximumProductSubarray", "322.CoinChange", "518.CoinChangeII", "350.IntersectionofTwoArraysII",
        "236.LowestCommonAncestorofaBinaryTree", "204.CountPrimes", "202.HappyNumber", "189.RotateArray",
        "207.CourseSchedule", "1306.JumpGameIII", "210.CourseScheduleII", "1431.KidsWiththeGreatestNumberofCandies"
    ],
    "Strings": [
        "3.LongestSubstringWithoutRepeatingCharacters", "5.LongestPalindromicSubstring",
        "17.LetterCombinationsofaPhoneNumber", "22.GenerateParentheses", "39.CombinationSum",
        "46.Permutations", "68.TextJustification", "76.MinimumWindowSubstring", "84.LargestRectangleinHistogram",
        "97.InterleavingString", "100.SameTree", "102.BinaryTreeLevelOrderTraversal", "114.FlattenBinaryTreetoLinkedList",
        "117.PopulatingNextRightPointersinEachNodeII", "121.BestTimetoBuyandSellStock", "122.BestTimetoBuyandSellStockII",
        "123.BestTimetoBuyandSellStockIII", "124.BinaryTreeMaximumPathSum", "128.LongestConsecutiveSequence",
        "132.PalindromePartitioningII", "131.PalindromePartitioning", "135.Candy", "146.LRUCache", "153.FindMinimuminRotatedSortedArray",
        "156.BinaryTreeUpsideDown", "165.CompareVersionNumbers", "169.MajorityElement", "171.ExcelSheetColumnNumber"
    ],
    "LinkedLists": [
        "2.AddTwoNumbers", "19.RemoveNthNodeFromEndofList", "21.MergeTwoSortedLists",
        "24.SwapNodesinPairs", "25.ReverseNodesink-Group", "26.RemoveDuplicatesfromSortedArray",
        "82.RemoveDuplicatesfromSortedListII", "83.RemoveDuplicatesfromSortedList", "86.PartitionList",
        "92.ReverseLinkedListII", "141.LinkedListCycle", "142.LinkedListCycleII", "143.ReorderList",
        "206.ReverseLinkedList", "237.DeleteNodeinaLinkedList", "328.OddEvenLinkedList", "430.FlattenaMultilevelDoublyLinkedList",
        "445.AddTwoNumbersII", "147.InsertionSortList", "156.BinaryTreeUpsideDown", "147.ReverseLinkedList"
    ],
    "Trees": [
        "104.MaximumDepthofBinaryTree", "105.ConstructBinaryTreefromPreorderandInorderTraversal",
        "106.ConstructBinaryTreefromInorderandPostorderTraversal", "111.MinimumDepthofBinaryTree",
        "112.PathSum", "113.PathSumII", "124.BinaryTreeMaximumPathSum", "145.BinaryTreePostorderTraversal",
        "199.BinaryTreeRightSideView", "226.InvertBinaryTree", "235.LowestCommonAncestorofaBinarySearchTree",
        "236.LowestCommonAncestorofaBinaryTree", "297.SerializeandDeserializeBinaryTree", "314.BinaryTreeVerticalOrderTraversal",
        "543.DiameterofBinaryTree", "572.SubtreeofAnotherTree", "993.CousinsinBinaryTree", "1022.SumofRootToLeafBinaryNumbers",
        "1008.ConstructBinarySearchTreefromPreorderTraversal", "1038.BinarySearchTreetoGreaterSumTree",
        "110.BalancedBinaryTree", "116.PopulatingNextRightPointersinEachNode", "437.PathSumIII"
    ],
    "Graphs": [
        "200.NumberofIslands", "207.CourseSchedule", "210.CourseScheduleII", "261.GraphValidTree",
        "743.NetworkDelayTime", "802.FindEventualSafeStates", "827.MakingALargeIsland", "841.KeysandRooms",
        "863.AllNodesDistanceKinBinaryTree", "994.RottingOranges", "1306.JumpGameIII", "207.CourseSchedule",
        "1192.CriticalConnectionsinaNetwork", "1369.GettheSecondMostRecentActivity", "2007.FindOriginalArrayFromDoubledArray"
    ],
    "DynamicProgramming": [
        "10.RegularExpressionMatching", "62.UniquePaths", "63.UniquePathsII", "70.ClimbingStairs",
        "121.BestTimetoBuyandSellStock", "122.BestTimetoBuyandSellStockII", "198.HouseRobber",
        "213.HouseRobberII", "300.LongestIncreasingSubsequence", "322.CoinChange", "333.LargestBSTSubtree",
        "437.PathSumIII", "463.IslandPerimeter", "502.IPO", "518.CoinChangeII", "646.MaximumLengthofaPairWithEqualSumofDigits"
    ],
    "Backtracking": [
        "22.GenerateParentheses", "39.CombinationSum", "46.Permutations", "47.PermutationsII",
        "77.Combinations", "78.Subsets", "79.WordSearch", "90.SubsetsII", "131.PalindromePartitioning",
        "216.CombinationSumIII", "261.GraphValidTree", "263.UglyNumber", "473.MatchstickstoSquare"
    ],
    "Sorting": [
        "912.SortanArray", "75.SortColors", "88.MergeSortedArray", "324.WiggleSortII", "451.SortCharactersByFrequency"
    ],
    "Mathematics": [
        "7.ReverseInteger", "9.PalindromeNumber", "50.Pow(x,n)", "62.UniquePaths", "125.ValidPalindrome",
        "258.AddDigits", "369.PlusOneLinkedList", "453.MinimumMovestoEqualArrayElements", "762.PrimeNumberofSetBitsinBinaryRepresentation"
    ],
    "Miscellaneous": [
        "1.TwoSum", "5.LongestPalindromicSubstring", "6.ZigzagConversion", "7.ReverseInteger",
        "9.PalindromeNumber", "10.RegularExpressionMatching", "11.ContainerWithMostWater", "12.IntegertoRoman",
        "13.RomantoInteger", "14.LongestCommonPrefix", "15.3Sum", "16.3SumClosest", "17.LetterCombinationsofaPhoneNumber",
        "18.4Sum", "19.RemoveNthNodeFromEndofList", "20.ValidParentheses", "21.MergeTwoSortedLists", "22.GenerateParentheses",
        "23.MergekSortedLists", "24.SwapNodesinPairs", "25.ReverseNodesink-Group", "26.RemoveDuplicatesfromSortedArray",
        "27.RemoveElement", "28.FindtheIndexoftheFirstOccurrenceinaString", "29.DivideTwoIntegers", "30.SubstringwithConcatenationofAllWords",
        "31.NextPermutation", "32.LongestValidParentheses", "33.SearchinRotatedSortedArray", "34.FindFirstandLastPositionofElementinSortedArray",
        "35.SearchInsertPosition", "36.ValidSudoku", "37.SudokuSolver", "38.CountandSay", "39.CombinationSum", "40.CombinationSumII"
    ]
}

def create_directory_structure_with_files(base_path, categories):
    for category, problems in categories.items():
        # Create category directory
        category_path = os.path.join(base_path, category)
        os.makedirs(category_path, exist_ok=True)

        for problem in problems:
            problem_path = os.path.join(category_path, f"{problem}.py")
            # Create an empty Python file for each problem
            with open(problem_path, 'w') as file:
                pass

if __name__ == "__main__":
    base_path = "Microsoft"
    create_directory_structure_with_files(base_path, categories)
