# LeetCode 88 - Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Replace empty tail of nums1 with nums2, then sort.
        Time:  O((m+n) log(m+n))
        Space: O(1) extra (in-place)
        """
        nums1[m:] = nums2
        nums1.sort()


# ─── Test it ─────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    # Test 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    sol.merge(nums1, 3, nums2, 3)
    print("Test 1:", nums1)  # Expected: [1, 2, 2, 3, 5, 6]

    # Test 2
    nums1 = [1]
    nums2 = []
    sol.merge(nums1, 1, nums2, 0)
    print("Test 2:", nums1)  # Expected: [1]

    # Test 3
    nums1 = [0]
    nums2 = [1]
    sol.merge(nums1, 0, nums2, 1)
    print("Test 3:", nums1)  # Expected: [1]