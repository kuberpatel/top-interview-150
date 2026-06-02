# LeetCode 26 - Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy
# Pattern: Two Pointers (Read/Write)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Array is sorted, so duplicates are adjacent.
        Keep element only if it differs from the last written value.
        Time:  O(n)
        Space: O(1)
        """
        if not nums:
            return 0

        write = 1  # first element is always kept
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write


# ─── Test it ─────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    nums = [1, 1, 2]
    k = sol.removeDuplicates(nums)
    print(f"Test 1: k={k}, nums={nums[:k]}")  # Expected: k=2, nums=[1,2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(nums)
    print(f"Test 2: k={k}, nums={nums[:k]}")  # Expected: k=5, nums=[0,1,2,3,4]
