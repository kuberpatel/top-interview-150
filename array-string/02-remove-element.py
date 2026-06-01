# LeetCode 27 - Remove Element
# https://leetcode.com/problems/remove-element/
# Difficulty: Easy
# Pattern: In-Place Modification

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        Filter out val using list comprehension, reassign in-place.
        Time:  O(n)
        Space: O(n) for the comprehension
        """
        nums[:] = [x for x in nums if x != val]
        return len(nums)


# ─── Test it ─────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()

    nums = [3, 2, 2, 3]
    k = sol.removeElement(nums, 3)
    print(f"Test 1: k={k}, nums={nums[:k]}")  # Expected: k=2, nums=[2,2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = sol.removeElement(nums, 2)
    print(f"Test 2: k={k}, nums={nums[:k]}")  # Expected: k=5, nums=[0,1,3,0,4]
