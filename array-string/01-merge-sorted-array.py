# LeetCode 88 - Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy
# Pattern: Two Pointers (or built-in sort for brute force)

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Approach: Replace empty tail of nums1 with nums2, then sort.
        Time:  O((m+n) log(m+n))  — dominated by sort
        Space: O(1) extra (in-place)
        """
        nums1[m:] = nums2
        nums1.sort()
