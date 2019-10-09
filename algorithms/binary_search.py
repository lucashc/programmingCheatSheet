# Binary search 
## \note Expects a sorted array
def bin_search(X, arr):
	low = 0
	high = len(arr)
	while (low < high):
		mid = (low + high)/2
		if arr[mid] == x:
			return mid
		elif X > arr[mid]:
			low = mid + 1
		else:
			high = mid
	return high
