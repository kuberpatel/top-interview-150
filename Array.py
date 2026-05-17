nums = [10,5,6,7,8,9]

# print(nums[0]) // 5
# print(nums[1]) // 6
# print (nums[-1]) // 8       //-1 = last element // -2 = second last
# nums[1] = 100    
# print(nums)                //update a value
# nums.append(9)             //add value in last
# print(nums)     
# nums.insert(1,10)          //Adds at specific position
# print(nums)
# nums.remove(8)             //used to delete a value from a list. 
# print(nums)       
# nums.pop()                 //used to delete last element
# print(nums)
# nums.pop(1)                //used to remove an item using its index.
# print(nums)
# len(nums)                  //gives the total number of items in a list (or string, tuple, etc.).
# print(nums)
# print(nums[1:4])             Slicing list[start:end]
#                              start → where to begin
#                              end → stop BEFORE this index
# for num in nums:
#     print(num)                 //Loop Through List
# print(8 in nums)               //Simple Search Using in
# nums.sort()                      //Ascending order.
# print(nums)
# nums.sort(reverse=True)          //Descending order
# print(nums)
# nums.reverse()                   // Reverse
# print(nums)
new_nums = nums.copy()
new_nums[0] = 100
print(nums)
print(new_nums)

