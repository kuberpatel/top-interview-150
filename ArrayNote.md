Python List (Array)
What is a List?

Python list = dynamic array.

nums = [5, 8, 2, 9, 3]
Features
Ordered
Mutable
Duplicates allowed
Index starts from 0
Memory Concept
[5][8][2][9][3]

Elements contiguous memory me store hote hain.

Result
Fast indexing → O(1)
Middle insert/delete slow → O(n)
Important Operations
Access
nums[0]
nums[-1]
0 → first element
-1 → last element
Complexity
O(1)
Update
nums[1] = 100
Complexity
O(1)
Append
nums.append(7)

End me add karta hai.

Complexity
O(1) amortized
Insert
nums.insert(1, 10)

Specific position par add.

Complexity
O(n)
Why Slow?

Elements shift hote hain.

Remove
By value
nums.remove(8)
By index
nums.pop(1)
Last element
nums.pop()
Length
len(nums)
Complexity
O(1)
Slicing
nums[1:4]
start included
end excluded
Loop
for num in nums:
print(num)
Search
8 in nums
Complexity
O(n)

One-by-one checking.

Sort
nums.sort()
Descending
nums.sort(reverse=True)
Complexity
O(n log n)
Reverse
nums.reverse()
Copy
Wrong
a = b

Same memory reference.

Correct
a = b.copy()
Time Complexities
Operation Complexity
Access O(1)
Update O(1)
Append O(1) amortized
Insert Middle O(n)
Delete Middle O(n)
Search O(n)
Sort O(n log n)
Important Concepts
Mutable
nums[0] = 99

Allowed.

Dynamic Array

Python automatically resize karta hai.

Manual memory management nahi karna padta.

Common Mistakes
Wrong
nums = []
nums[0] = 5
Correct
nums.append(5)
remove() Error
nums.remove(100)

Value exist nahi karegi to error aayega.

append vs insert
append() → end
insert() → specific index
TypeScript Same Concept
let nums: number[] = [5,8,2];

nums.push(7);
nums[0];
Real-Life Usage
E-commerce
cart_items = ["Phone", "Laptop"]
Food Delivery
active_orders = [101, 102, 103]
Chat App
messages = []
messages.append("Hello")
Interview Summary

Python lists are dynamic arrays with fast indexing due to contiguous memory storage, but middle insertions and deletions are slow because elements must shift.
