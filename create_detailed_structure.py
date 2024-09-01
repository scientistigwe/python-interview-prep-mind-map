import os

# Define the problems categorized by type and subcategory
problems_by_category = {
    "Array": {
        "Sorting and Searching": [
            "33.SearchinRotatedSortedArray", "215.KthLargestElementinaArray", "704.BinarySearch",
            "34.FindFirstandLastPositionofElementinSortedArray", "240.Searcha2DMatrixII",
            "153.FindMinimuminRotatedSortedArray", "4.MedianofTwoSortedArrays", "780.ReachingPoints",
            "1010.PairsofSongsWithTotalDurationsDivisibleby60", "166.FractiontoRecurringDecimal"
        ],
        "Subarray and Sliding Window": [
            "42.TrappingRainWater", "560.SubarraySumEqualsK", "76.MinimumWindowSubstring",
            "209.MinimumSizeSubarraySum", "845.LongestMountaininArray", "239.SlidingWindowMaximum"
        ],
        "Miscellaneous": [
            "1356.SortIntegersbyTheNumberof1Bits", "896.MonotonicArray", "1389.CreateTargetArrayinTheGivenOrder",
            "118.PascalsTriangle", "118.PascalsTriangleII", "121.BestTimetoBuyandSellStock",
            "2087.MinimumCostHomecomingofaRobotinaGrid", "2420.FindAllGoodIndices",
            "3001.MinimumMovestoCaptureTheQueen", "2550.CountCollisionsOfMonkeysonaPolygon"
        ]
    },
    "String": {
        "Substrings and Subsequences": [
            "5.LongestPalindromicSubstring", "394.DecodeString", "131.PalindromePartitioning",
            "1163.LastSubstringinLexicographicalOrder", "516.LongestPalindromicSubsequence",
            "647.PalindromicSubstrings", "1328.BreakaPalindrome"
        ],
        "Pattern Matching": [
            "76.MinimumWindowSubstring", "459.RepeatedSubstringPattern", "28.ImplementstrStr",
            "567.PermutationinString"
        ],
        "String Manipulation": [
            "344.ReverseString", "143.ReorderList", "1370.IncreasingDecreasingString",
            "267.PalindromePermutationII", "125.ValidPalindrome", "583.DeleteOperationforTwoStrings",
            "443.StringCompression", "2484.CountPalindromicSubsequences"
        ]
    },
    "Dynamic Programming": {
        "Classic Problems": [
            "62.UniquePaths", "63.UniquePathsII", "64.MinimumPathSum", "152.MaximumProductSubarray",
            "279.PerfectSquares", "322.CoinChange"
        ],
        "Sequences": [
            "300.LongestIncreasingSubsequence", "115.DistinctSubsequences", "174.DungeonGame",
            "53.MaximumSubarray", "516.LongestPalindromicSubsequence"
        ],
        "Knapsack and Similar": [
            "309.BestTimetoBuyandSellStockwithCooldown", "322.CoinChange", "518.CoinChangeII",
            "123.BestTimetoBuyandSellStockIII", "188.BestTimetoBuyandSellStockIV",
            "887.SuperEggDrop"
        ],
        "Miscellaneous": [
            "2087.MinimumCostHomecomingofaRobotinaGrid", "2420.FindAllGoodIndices",
            "122.BestTimetoBuyandSellStockII", "1109.CorporateFlightBookings", "2191.SorttheJumbledNumbers",
            "1427.PerformStringShifts", "1413.MinimumValuetoGetPositiveStepbyStepSum",
            "1750.MinimumLengthofStringAfterDeletingSimilarEnds", "1771.MaximizePalindromeLengthFromSubsequences",
            "2266.CountNumberofTexts", "2300.SuccessfulPairsofSpellsandPotions",
            "2446.DetermineifTwoEventsHaveConflict", "2550.CountCollisionsOfMonkeysonaPolygon",
            "3168.MinimumNumberofChairsinaWaitingRoom", "2933.High-AccessEmployees"
        ]
    },
    "Linked List": {
        "Basic Operations": [
            "206.ReverseLinkedList", "21.MergeTwoSortedLists", "19.RemoveNthNodeFromEndofList",
            "83.RemoveDuplicatesfromSortedList", "160.IntersectionofTwoLinkedLists"
        ],
        "Advanced Operations": [
            "23.MergekSortedLists", "141.LinkedListCycle", "142.LinkedListCycleII", "25.ReverseNodesink-Group"
        ],
        "Intersection and Cycle": [
            "160.IntersectionofTwoLinkedLists", "142.LinkedListCycleII", "287.FindtheDuplicateNumber",
            "1836.RemoveDuplicatesFromanUnsortedLinkedList"
        ]
    },
    "Graph": {
        "Basic Traversal": [
            "207.CourseSchedule", "133.CloneGraph", "210.CourseScheduleII", "200.NumberofIslands",
            "417.PacificAtlanticWaterFlow"
        ],
        "Shortest Path": [
            "743.NetworkDelayTime", "785.IsGraphBipartite", "1514.PathwithMaximumProbability",
            "126.WordLadderII", "207.CourseSchedule", "743.NetworkDelayTime"
        ],
        "Minimum Spanning Tree": [
            "1135.MinimumCosttoConnectSticks", "1136.ParallelCourses", "785.IsGraphBipartite"
        ]
    },
    "Tree": {
        "Binary Tree Traversal": [
            "101.SymmetricTree", "102.BinaryTreeLevelOrderTraversal", "104.MaximumDepthofBinaryTree",
            "297.SerializeandDeserializeBinaryTree", "113.PathSumII"
        ],
        "Binary Search Tree": [
            "230.KthSmallestElementinaBST", "108.ConvertSortedArraytoBinarySearchTree",
            "701.InsertintoABinarySearchTree", "270.ClosestBinarySearchTreeValue"
        ],
        "Advanced Tree Problems": [
            "124.BinaryTreeMaximumPathSum", "863.AllNodesDistanceKinaBinaryTree", "814.BinaryTreePruning",
            "545.BordersofBinaryTree", "938.RangeSumofBST"
        ]
    },
    "Math": {
        "Basic Arithmetic": [
            "326.PowerofThree", "7.ReverseInteger", "9.PalindromeNumber", "50.Pow(x, n)",
            "67.AddBinary", "8.StringtoInteger(atoi)", "2.AddTwoNumbers", "6.ZigzagConversion"
        ],
        "Geometry and Combinatorics": [
            "59.SpiralMatrixII", "48.RotateImage", "54.SpiralMatrix", "240.Searcha2DMatrixII",
            "738.MonotonicArray", "238.ProductofArrayExceptSelf"
        ]
    }
}

# Function to create directories and files based on category and subcategory
def create_files_by_category(base_path, problems_dict):
    for category, subcategories in problems_dict.items():
        category_path = os.path.join(base_path, category)
        os.makedirs(category_path, exist_ok=True)

        for subcategory, problems in subcategories.items():
            subcategory_path = os.path.join(category_path, subcategory)
            os.makedirs(subcategory_path, exist_ok=True)

            for problem in problems:
                problem_filename = f"{problem}.py"
                problem_path = os.path.join(subcategory_path, problem_filename)
                open(problem_path, 'w').close()  # Create an empty .py file


# Set the base directory path where files will be created
base_directory = 'Goldman-Sachs'
create_files_by_category(base_directory, problems_by_category)

print("Directories and files have been created successfully.")
