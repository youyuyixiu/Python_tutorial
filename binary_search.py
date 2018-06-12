def binary_search(search_list,target):
	left = 0
	right = len(search_list) - 1
	while left <= right:
		mid = (left + right) // 2
		if search_list[mid] < target:
			left = mid + 1
		if search_list[mid] == target:
			return mid
		if search_list[mid] > target:
			right = mid - 1
	return None


search_list = [1,3,6,7,9,11]
print(binary_search(search_list,0))
print(binary_search(search_list,1))
print(binary_search(search_list,3))
print(binary_search(search_list,6))
print(binary_search(search_list,7))
print(binary_search(search_list,9))
print(binary_search(search_list,11))