# # l = [2,5,3,1,4,7,8]

# # key = 5

# # def linear_search(key,l):
# #     # found = False
# #     # for i in l:
# #     #     if key == i:
# #     #         found = True
# #     # return found
# #     return key in l


# # print(linear_search(key,l))

# # binary search

# li = [2,5,3,1,4,7,8]
# li.sort()
# k = 5
# def binary_search(key,ls):
#     found = False
#     le = len(ls)
#     i = ls[0]
#     j = ls[-1]
#     l = le // 2
#     while(found == False):
        
#         if key == l:
#             found = True
#             break
#         elif key > l:
#             i = l + 1
#         else:
#             j = l - 1

#     return found

# print(binary_search(k,li))

# Iterative Binary Search Function 
# It returns index of x in given array arr if present, 
# else returns -1 
def binary_search(arr, x): 
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high: 

		mid = (high + low) // 2

		# Check if x is present at mid 
		if arr[mid] < x: 
			low = mid + 1

		# If x is greater, ignore left half 
		elif arr[mid] > x: 
			high = mid - 1

		# If x is smaller, ignore right half 
		else: 
			return mid 

	# If we reach here, then the element was not present 
	return -1


# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2

# Function call 
result = binary_search(arr, x) 

if result != -1: 
	print("Element is present at index", str(result)) 
else: 
	print("Element is not present in array") 
