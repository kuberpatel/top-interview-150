# Python List (Array) — Precise Notes

python
# Python List = Dynamic Array
# Ordered, mutable, allows duplicates

nums = [10, 5, 6, 7, 8, 9]

# ---------------- ACCESS ----------------

print(nums[0])      # 10 → Access first element (O(1))
print(nums[1])      # 5
print(nums[-1])     # 9 → Last element
print(nums[-2])     # 8 → Second last element

# ---------------- UPDATE ----------------

nums[1] = 100       # Update value using index (O(1))
print(nums)

# ---------------- ADD ELEMENTS ----------------

nums.append(11)     # Add at end (O(1) amortized)
print(nums)

nums.insert(1, 50)  # Add at specific index (O(n))
print(nums)

# ---------------- DELETE ELEMENTS ----------------

nums.remove(8)      # Remove by value (O(n))
print(nums)

nums.pop()          # Remove last element (O(1))
print(nums)

nums.pop(1)         # Remove using index (O(n))
print(nums)

# ---------------- LENGTH ----------------

print(len(nums))    # Total number of elements (O(1))

# ---------------- SLICING ----------------

print(nums[1:4])    # start included, end excluded

# ---------------- LOOP ----------------

for num in nums:
    print(num)

# ---------------- SEARCH ----------------

print(8 in nums)    # Returns True/False (O(n))

# ---------------- SORTING ----------------

nums.sort()         # Ascending order (O(n log n))
print(nums)

nums.sort(reverse=True)   # Descending order
print(nums)

# ---------------- REVERSE ----------------

nums.reverse()      # Reverse list
print(nums)

# ---------------- COPY ----------------

new_nums = nums.copy()   # Create separate copy

new_nums[0] = 100

print(nums)
print(new_nums)

# =========================================================
# REAL-LIFE EXAMPLES
# =========================================================

# E-commerce App
cart_items = ["Phone", "Laptop"]

# Food Delivery App
active_orders = [101, 102, 103]

# Chat App
messages = []
messages.append("Hello")

# =========================================================
# IMPORTANT CONCEPTS
# =========================================================

# Python lists are dynamic arrays.
# Elements are stored contiguously in memory.

# Fast Operations:
# Access by index → O(1)
# Append at end → O(1) amortized

# Slow Operations:
# Insert/Delete in middle → O(n)
# Search in unsorted list → O(n)

# =========================================================
# INTERVIEW SUMMARY
# =========================================================

# Python lists are dynamic arrays that provide fast indexing
# because elements are stored contiguously in memory,
# but middle insertions/deletions are slow due to shifting.

