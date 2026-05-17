Python List (Array) — Complete Easy Notes in Hinglish
What is Python List?

Python me list ek dynamic array hoti hai.

nums = [5, 8, 2, 9, 3]
Ordered collection
Duplicate allowed
Index starts from 0
Mutable (change kar sakte ho)
Real-Life Example

Shopping cart:

[Milk, Bread, Eggs]

Har item ka position/index hota hai.

Memory Concept

Python list internally array ki tarah kaam karti hai.

[5][8][2][9][3]

Sab values contiguous memory me hoti hain.

Isi wajah se:

Index access fast
Middle insertion slow
Important Operations

1. Access Element
   nums = [5, 8, 2]

print(nums[0]) # 5
print(nums[2]) # 2
Time Complexity
O(1)
Why Fast?

Computer direct jump karta hai memory location par.

2. Negative Indexing
   nums[-1]

Output:

3
Meaning
-1 = last element
-2 = second last

Useful in interviews.

3. Update Value
   nums[1] = 100

Before:

[5,8,2]

After:

[5,100,2] 4. Append
nums.append(7)

Output:

[5,8,2,7]
Complexity
O(1) amortized
Why Fast?

Bas end me add hota hai.

No shifting.

5. Insert
   nums.insert(1, 10)

Output:

[5,10,8,2]
Complexity
O(n)
Why Slow?

Baaki elements shift hote hain.

6. Delete
   remove()
   nums.remove(8)

Value remove karta hai.

pop()
nums.pop()

Last element remove.

Fast.

pop(index)
nums.pop(1)

Middle delete → shifting.

Slow.

7. Length
   len(nums)
   Complexity
   O(1)

Python internally length maintain karta hai.

8. Slicing
   nums[1:4]

Output:

[8,2,9]
Meaning
start included
end excluded 9. Loop Through List
for num in nums:
print(num) 10. Search
8 in nums
Complexity
O(n)

Why?

One-by-one check.

11. Sort
    nums.sort()

Ascending order.

Descending
nums.sort(reverse=True) 12. Reverse
nums.reverse() 13. Copy List

Wrong way:

a = b

Both same memory use karenge.

Correct:

a = b.copy()
Common Interview Complexities
Operation Complexity
Access O(1)
Update O(1)
Append O(1) amortized
Insert Middle O(n)
Delete Middle O(n)
Search O(n)
Sort O(n log n)
Important Interview Concepts
Mutable
nums[0] = 99

Allowed.

List mutable hai.

Dynamic Array

Python automatically size increase karta hai.

Tum manually memory manage nahi karte.

Common Beginner Mistakes
Mistake 1
nums = []
nums[0] = 5

Error.

Pehle element exist hona chahiye.

Correct:

nums.append(5)
Mistake 2
nums.remove(100)

Agar value nahi hai → error.

Mistake 3

Confusing append vs insert

append() → end
insert() → specific position
TypeScript Comparison
let nums: number[] = [5,8,2];

nums.push(7);
nums[0];

Same concepts.

Real Project Usage
E-commerce
cart_items = ["Phone", "Laptop"]
Food Delivery
active_orders = [101, 102, 103]
Chat App
messages = []
messages.append(new_message)
One-Line Interview Summary

Python lists are dynamic arrays that provide fast indexing because elements are stored contiguously, but middle insertions/deletions are slow due to shifting elements.
