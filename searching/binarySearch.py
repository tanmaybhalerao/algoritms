#	BINARY SEARCH(recusively)
def binarySearch(start,end,array,item):
	#terminating condition
	if start>end:
		print("Not found")
		return
	#middle value of array
	mid = (start+end)//2
	if array[mid] == item:
		print("found at "+str(mid+1))
	elif array[mid]>item:
		#if value is less middle value check starting half array
		binarySearch(start,mid-1,array,item)
	else:
		#if value is greater than middle value check ending half array
		binarySearch(mid+1,end,array,item)

#input initialization
arr = [1,12,23,43,56]
item = 23 
#call function
binarySearch(0,len(arr),arr,item)
=========================OUTPUT=========================

Found at 3
