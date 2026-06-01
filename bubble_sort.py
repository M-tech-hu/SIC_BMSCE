input_numbers = []
for i in range(0,n-2):
#being at n-2 we acess n-1 element when comparing
	for j in range(0 , n-2-i) :#Acess elements of unsorted array
		if list[j]>list[j+1]:
			list[j],list[j+1]=list[j+1],list[j]