def linearSearch(array,item):
	for i in range(len(array)):	#for parsing whole array
		if item == array[i]:	#compare with item to array elements
			print(str(item)+" found at "+str(i)+" position in array")
			return						
	print("Not found")					

#input initialization
array = [1,12,43,56,23]
item = 23

#calling search function
linearSearch(array,item)

