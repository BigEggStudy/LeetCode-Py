[![AppVeyor Build Status](https://img.shields.io/appveyor/ci/bigegg/leetcode-py.svg?style=flat-square&label=Windows%20Build%20Status&logo=AppVeyor)](https://ci.appveyor.com/project/BigEgg/leetcode-py)
[![Travis Build Status](https://img.shields.io/badge/Linux%20Build%20Status-Invalid-lightgrey.svg?label=Linux%20Build%20Status&logo=travis&style=flat-square)]()
[![Solved Problems](https://img.shields.io/badge/Solved%20Problems-83-blue.svg?style=flat-square)](https://github.com/BigEggStudy/LeetCode-Py)

# LeetCode
The Python3 solutions for LeetCode problems.

## Problems

### Table of Contents
* [001-050](#Problems-001-050)
* [051-100](#Problems-051-100)
* [201-250](#Problems-201-250)
* [401-450](#Problems-401-450)
* [451-500](#Problems-451-500)
* [801-850](#Problems-801-850)
* [1001-1050](#Problems-1001-1050)
* [1051-1100](#Problems-1051-1100)
* [1151-1200](#Problems-1151-1200)

### Problems 001-050
[Back to Table of Contents](#Table-of-Contents)

| # | Title | Solutions | Time | Space | Comments |
|---| ----- | --------- | ---- | ----- | -------- |
| 1 | Two Sum | [Python3](./LeetCode/_0001_0050/_001_TwoSum.py)(40ms) | O(N) | O(N) | |
| 2 | Add Two Numbers | [Python3](./LeetCode/_0001_0050/_002_AddTwoNumbers.py)(112ms) | O(Max(N, M)) | O(1) | |
| 3 | Longest Substring Without Repeating Characters | [Python3](./LeetCode/_0001_0050/_003_LongestSubstringWithoutRepeatingCharacters.py)(72ms) | O(N) | O(1) | C# use array will slower |
| 4 | Median of Two Sorted Arrays | [Python3](./LeetCode/_0001_0050/_004_MedianOfTwoSortedArrays.py)(100ms) | O(Log(N+M)) | O(1) | |
| 5 | Longest Palindromic Substring | [Python3](./LeetCode/_0001_0050/_005_LongestPalindromicSubstring.py)(120ms) | O(N) | O(N) | Use Manacher's Algorithm |
| 6 | ZigZag Conversion | [Python3](./LeetCode/_0001_0050/_006_ZigZagConversion.py)(100ms) | O(N) | O(N) | |
| 7 | Reverse Integer | [Python3](./LeetCode/_0001_0050/_007_ReverseInteger.py)(32ms) | O(1) | O(1) | |
| 8 | String to Integer (atoi) | [Python3](./LeetCode/_0001_0050/_008_StringToInteger_atoi.py)(40ms) | O(1) | O(1) | |
| 9 | Palindrome Number | [Python3](./LeetCode/_0001_0050/_009_PalindromeNumber.py)(68ms) | O(1) | O(1) | |
| 10 | Regular Expression Matching | [Python3](./LeetCode/_0001_0050/_010_RegularExpressionMatching.py)(48ms) | O(N*M) | O(N*M) | |
| 11 | Container With Most Water | [Python3](./LeetCode/_0001_0050/_011_ContainerWithMostWater.py)(40ms) | O(N) | O(1) | |
| 12 | Integer to Roman | [Python3](./LeetCode/_0001_0050/_012_IntegerToRoman.py)(44ms) | O(N) | O(1) | |
| 13 | Roman to Integer | [Python3](./LeetCode/_0001_0050/_013_RomanToInteger.py)(56ms) | O(N) | O(1) | |
| 14 | Longest Common Prefix | [Python3](./LeetCode/_0001_0050/_014_LongestCommonPrefix.py)(32ms) | O(N) | O(1) | |
| 15 | 3Sum | [Python3](./LeetCode/_0001_0050/_015_3Sum.py)(400ms) | O(N<sup>2</sup>) | O(M) | For Python solution, use count to reduce time to O(min(N, M<sup>2</sup>)) and space to O(M) |
| 16 | 3Sum Closest | [Python3](./LeetCode/_0001_0050/_016_3SumClosest.py)(92ms) | O(N<sup>2</sup>) | O(1) | |
| 17 | Letter Combinations of a Phone Number | [Python3](./LeetCode/_0001_0050/_017_LetterCombinationsOfAPhoneNumber.py)(36ms) | O(4<sup>N</sup>) | O(4<sup>N</sup>) | |
| 18 | 4Sum | [Python3](./LeetCode/_0001_0050/_018_4Sum.py)(64ms) | O(N<sup>2</sup>) | O(N<sup>2</sup>) | |
| 19 | Remove Nth Node From End of List | [Python3](./LeetCode/_0001_0050/_019_RemoveNthNodeFromEndOfList.py)(32ms) | O(N) | O(1) | |
| 20 | Valid Parentheses | [Python3](./LeetCode/_0001_0050/_020_ValidParentheses.py)(36ms) | O(N) | O(N) | |
| 21 | Merge Two Sorted Lists | [Python3](./LeetCode/_0001_0050/_021_MergeTwoSortedLists.py)(40ms) | O(N<sub>1</sub>+N<sub>2</sub>) | O(1) | |
| 22 | Generate Parentheses | [Python3](./LeetCode/_0001_0050/_022_GenerateParentheses.py)(36ms) | O(N) | O(?) | |
| 23 | Merge k Sorted Lists | [Python3](./LeetCode/_0001_0050/_023_MergeKSortedLists.py)(64ms) | O(N*logk) | O(1) | Python solution use heap to compare the lists, so reduce time to O(N logK) but increase space to O(k) |
| 24 | Swap Nodes in Pairs | [Python3](./LeetCode/_0001_0050/_024_SwapNodesInPairs.py)(28ms) | O(N) | O(1) | |
| 25 | Reverse Nodes in k-Group | [Python3](./LeetCode/_0001_0050/_025_ReverseNodesInKGroup.py)(48ms) | O(N) | O(1) | |
| 26 | Remove Duplicates from Sorted Array | [Python3](./LeetCode/_0001_0050/_026_RemoveDuplicatesFromSortedArray.py)(52ms) | O(N) | O(1) | |
| 27 | Remove Element | [Python3](./LeetCode/_0001_0050/_027_RemoveElement.py)(28ms) | O(N) | O(1) | |
| 28 | Implement strStr() | [Python3](./LeetCode/_0001_0050/_028_ImplementStrStr.py)(32ms) | O(N+M) | O(1) | Use Knuth–Morris–Pratt Algorithm |
| 29 | Divide Two Integers | [Python3](./LeetCode/_0001_0050/_029_DivideTwoIntegers.py)(32ms) | O(N) | O(1) | |
| 30 | Substring with Concatenation of All Words | [Python3](./LeetCode/_0001_0050/_030_SubstringWithConcatenationOfAllWords.py)(56ms) | O(N*M) | O(M) | |
| 31 | Next Permutation | [Python3](./LeetCode/_0001_0050/_031_NextPermutation.py)(36ms) | O(N) | O(1) | |
| 32 | Longest Valid Parentheses | [Python3](./LeetCode/_0001_0050/_032_LongestValidParentheses.py)(48ms) | O(N) | O(1) | |
| 33 | Search in Rotated Sorted Array | [Python3](./LeetCode/_0001_0050/_033_SearchInRotatedSortedArray.py)(28ms) | O(N) | O(1) | |
| 34 | Search for a Range | [Python3](./LeetCode/_0001_0050/_034_SearchForARange.py)(32ms) | O(LogN) | O(1) | |
| 35 | Search Insert Position | [Python3](./LeetCode/_0001_0050/_035_SearchInsertPosition.py)(28ms) | O(LogN) | O(1) | |
| 36 | Valid Sudoku | [Python3](./LeetCode/_0001_0050/_036_ValidSudoku.py)(44ms) | O(1) | O(1) | |
| 37 | Sudoku Solver | [Python3](./LeetCode/_0001_0050/_037_SudokuSolver.py)(44ms) | O(1) | N(1) | |
| 38 | Count and Say | [Python3](./LeetCode/_0001_0050/_038_CountAndSay.py)(32ms) | O(N<sup>2</sup>) | O(N) | Python use an dictionary of answers |
| 39 | Combination Sum | [Python3](./LeetCode/_0001_0050/_039_CombinationSum.py)(52ms) | O(N!) | O(N) | |
| 40 | Combination Sum II | [Python3](./LeetCode/_0001_0050/_040_CombinationSum2.py)(48ms) | O(N!) | O(N) | |
| 41 | First Missing Positive | [Python3](./LeetCode/_0001_0050/_041_FirstMissingPositive.py)(36ms) | O(N) | O(1) | |
| 42 | Trapping Rain Water | [Python3](./LeetCode/_0001_0050/_042_TrappingRainWater.py)(32ms) | O(N) | O(1) | |
| 43 | Multiply Strings | [Python3](./LeetCode/_0001_0050/_043_MultiplyStrings.py)(84ms) | O(N*M) | O(N+M) | |
| 44 | Wildcard Matching | [Python3](./LeetCode/_0001_0050/_044_WildcardMatching.py)(60ms) | O(N*M) | O(1) | Similar with [Problem No. 10](./Problems/0001-0050/010-RegularExpressionMatching.md) |
| 45 | Jump Game II | [Python3](./LeetCode/_0001_0050/_045_JumpGame2.py)(40ms) | O(N) | O(1) | Use Greedy Algorithm |
| 46 | Permutations | [Python3](./LeetCode/_0001_0050/_046_Permutations.py)(44ms) | O(N!) | (N) | Get inspired by [Heap's Algorithm](https://en.wikipedia.org/wiki/Heap%27s_algorithm) |
| 47 | Permutations II | [Python3](./LeetCode/_0001_0050/_047_Permutations2.py)(56ms) | O(N!) | (N) | Get inspired by [Heap's Algorithm](https://en.wikipedia.org/wiki/Heap%27s_algorithm) |
| 48 | Rotate Image | [Python3](./LeetCode/_0001_0050/_048_RotateImage.py)(32ms) | O(N<sup>2</sup>) | O(1) | |
| 49 | Group Anagrams | [Python3](./LeetCode/_0001_0050/_049_GroupAnagrams.py)(108ms) | O(N K log K) | O(N K) | Linear algorithm will slower and cost more memory |
| 50 | Pow(x, n) | [Python3](./LeetCode/_0001_0050/_050_Pow.py)(32ms) | O(LogN) | O(1) | |

### Problems 051-100
[Back to Table of Contents](#Table-of-Contents)

| # | Title | Solutions | Time | Space | Comments |
|---| ----- | --------- | ---- | ----- | -------- |
| 51 | N-Queens | [Python3](./LeetCode/_0051_0100/_051_NQueens.py)(60ms) | O(N!) | O(N) | |
| 52 | N-Queens II | [Python3](./LeetCode/_0051_0100/_052_NQueens2.py)(44ms) | O(N!) | O(N) | |
| 53 | Maximum Subarray | [Python3](./LeetCode/_0051_0100/_053_MaximumSubarray.py)(36ms) | O(N) | O(1) | |
| 54 | Spiral Matrix | [Python3](./LeetCode/_0051_0100/_054_SpiralMatrix.py)(28ms) | O(N) | O(1) | |
| 55 | Jump Game | [Python3](./LeetCode/_0051_0100/_055_JumpGame.py)(32ms) | O(N) | O(1) | Use Greedy Algorithm |
| 56 | Merge Intervals | [Python3](./LeetCode/_0051_0100/_056_MergeIntervals.py)(40ms) | O(NLogN) | O(1) | |
| 57 | Insert Interval | [Python3](./LeetCode/_0051_0100/_057_InsertInterval.py)(40ms) | O(N) | O(N) | |
| 58 | Length of Last Word | [Python3](./LeetCode/_0051_0100/_058_LengthOfLastWord.py)(32ms) | O(N) | O(1) | |
| 59 | Spiral Matrix II | [Python3](./LeetCode/_0051_0100/_059_SpiralMatrix2.py)(36ms) | O(N<sup>2</sup>) | O(N<sup>2</sup>) | |
| 60 | Permutation Sequence | [Python3](./LeetCode/_0051_0100/_060_PermutationSequence.py)(24ms) | O(N) | (N) | Use Cantor Expansion (Introduction to Algorithms, MIT) |
| 61 | Rotate List | [Python3](./LeetCode/_0051_0100/_061_RotateList.py)(36ms) | O(N) | O(1) | |
| 62 | Unique Paths | [Python3](./LeetCode/_0051_0100/_062_UniquePaths.py)(28ms) | O(Min(M, N)) | O(1) | Use dynamic programing will cost O(M*N) time and O(Min(M, N)) space |
| 63 | Unique Paths II | [Python3](./LeetCode/_0051_0100/_063_UniquePaths2.py)(32ms) | O(M*N) | O(Min(M, N)) | |
| 64 | Minimum Path Sum | [Python3](./LeetCode/_0051_0100/_064_MinimumPathSum.py)(100ms) | O(M*N) | O(Min(M, N)) | Update grid to not use new space |
| 65 | Valid Number | [Python3](./LeetCode/_0051_0100/_065_ValidNumber.py)(36ms) | O(N) | O(1) | |
| 66 | Plus One | [Python3](./LeetCode/_0051_0100/_066_PlusOne.py)(36ms) | O(N) | O(N) | |
| 67 | Add Binary | [Python3](./LeetCode/_0051_0100/_067_AddBinary.py)(40ms) | O(N) | O(N) | |
| 68 | Text Justification | [Python3](./LeetCode/_0051_0100/_068_TextJustification.py)(32ms) | O(N) | O(N) | |
| 69 | Sqrt(x) | [Python3](./LeetCode/_0051_0100/_069_Sqrt_X.py)(36ms) | O(LogN) | O(1) | Use [Newton–Raphson Method](https://en.wikipedia.org/wiki/Newton%27s_method) to [computing square root](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots) |
| 70 | Climbing Stairs | [Python3](./LeetCode/_0051_0100/_070_ClimbingStairs.py)(28ms) | O(N) | O(1) | |
| 71 | Simplify Path | [Python3](./LeetCode/_0051_0100/_071_SimplifyPath.py)(32ms) | O(N) | O(N) | |
| 72 | Edit Distance | [Python3](./LeetCode/_0051_0100/_072_EditDistance.py)(128ms) | O(N*M) | O(Min(N,M)) | |
| 73 | Set Matrix Zeroes | [Python3](./LeetCode/_0051_0100/_073_SetMatrixZeroes.py)(148ms) | O(N*M) | O(N+M) | When use constant space, solution will slower |
| 74 | Search a 2D Matrix | [Python3](./LeetCode/_0051_0100/_074_SearchA2DMatrix.py)(76ms) | O(Log(N+M)) | O(1) | |
| 75 | Sort Colors | [Python3](./LeetCode/_0051_0100/_075_SortColors.py)(32ms) | O(N) | O(1) | |

### Problems 201-250
[Back to Table of Contents](#Table-of-Contents)

| # | Title | Solutions | Time | Space | Comments |
|---| ----- | --------- | ---- | ----- | -------- |
| 222 | Count Complete Tree Nodes | [Python3](./LeetCode/_0201_0250/_0222_CountCompleteTreeNodes.py)(80ms) | O(log<sup>2</sup>N) | O(1) | |

### Problems 401-450
[Back to Table of Contents](#Table-of-Contents)

| # | Title | Solutions | Time | Space | Comments |
|---| ----- | --------- | ---- | ----- | -------- |
| 410 | Split Array Largest Sum | [Python3](./LeetCode/_0401_0450/_0410_SplitArrayLargestSum.py)(40ms) | O(N∗log(sum of array)) | O(1) | Binary Search |

### Problems 451-500
[Back to Table of Contents](#Table-of-Contents)

| # | Title | Solutions | Time | Space | Comments |
|---| ----- | --------- | ---- | ----- | -------- |
| 482 | License Key Formatting | [Python3](./LeetCode/_0451_0500/_0482_LicenseKeyFormatting.py)(36ms) | O(N) | O(N) | |

### Problems 801-850
[Back to Table of Contents](#Table-of-Contents)

| # | Title | Solutions | Time | Space | Comments |
|---| ----- | --------- | ---- | ----- | -------- |
| 843 | Guess the Word | [Python3](./LeetCode/_0801_0850/_0843_GuesstheWord.py)(36ms) | O(N<sup>2</sup>) | O(N) | |

### Problems 1001-1050
[Back to Table of Contents](#Table-of-Contents)

| # | Title | Solutions | Time | Space | Comments |
|---| ----- | --------- | ---- | ----- | -------- |
| 1007 | Minimum Domino Rotations For Equal Row | [Python3](./LeetCode/_1001_1050/_1007_MinimumDominoRotationsForEqualRow.py)(1248ms) | O(N) | O(1) | |

### Problems 1051-1100
[Back to Table of Contents](#Table-of-Contents)

| # | Title | Solutions | Time | Space | Comments |
|---| ----- | --------- | ---- | ----- | -------- |
| 1057 | Campus Bikes | [Python3](./LeetCode/_1051_1100/_1057_CampusBikes.py)(724ms) | O(N*M) | O(N*M) | |
| 1096 | Brace Expansion II | [Python3](./LeetCode/_1051_1100/_1096_BraceExpansionII.py)(48ms) | O(N) | ? | |

### Problems 1151-1200
[Back to Table of Contents](#Table-of-Contents)

| # | Title | Solutions | Time | Space | Comments |
|---| ----- | --------- | ---- | ----- | -------- |
| 1197 | Minimum Knight Moves | [Python3](./LeetCode/_1151_1200/_1197_MinimumKnightMoves.py)(36ms) | O(N<sup>2</sup>) | O(N<sup>2</sup>) | |
