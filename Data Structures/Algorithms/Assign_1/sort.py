
import numpy as np 
import matplotlib.pyplot as plt

# arr1 = [2,4,1,5,6]
# arr2 = [2,4,1,5,6]

def selection(arr):
	count =  0 
	swap = 0
	length = len(arr) 
	for i in range(length-1):		
		min = i 
		for j in range(i,length):
			count+=1
			if arr[min]>arr[j]:
				min = j
				
		arr[i],arr[min] = arr[min],arr[i]
		swap+=1
		 
	# print(arr)
	# print("Selection count : ",count)
	# print("Selection swaps : ",swap)
	# print("-------------------------------")
	return [count,swap]

def bubble(arr):
	count =  0 
	swap = 0
	length = len(arr)
	for i in range (length-1) :	
		for j in range(length-i-1):
			count+=1
			if arr[j] > arr[j + 1] :
				swap+=1
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				
	# print("Selection count : ",count)
	# print("Selection swaps : ",swap)
	# print("-------------------------------")
	return [count,swap]


def insertion(arr):
	count =  0 
	swap = 0
	length = len(arr) 
	for i in range(length):
		count+=1
		j = i-1
		temp = arr[i]
		while j>=0 and arr[j]>temp:
			arr[j+1] = arr[j]
			j-=1
		arr[j+1] = temp
		swap+=1
	print(arr)
	print("Insertion count : ",count)
	print("Insertion swaps : ",swap)



xpoints = [] 
ypoints = []
zpoints = []

for i in range(1,100):
	rand_int = np.random.randint(0,1000,size=(i)) 
	xpoints.append(i)
	temp_array = bubble(rand_int)
	ypoints.append(temp_array[0])
	zpoints.append(temp_array[1])


plt.plot(xpoints, ypoints,label ='count-line')
plt.plot(xpoints, zpoints,label ='swap-line')
plt.plot(xpoints,[i*i for i in range(1,100)],label ='n-square-line')
plt.xlabel("Array Size")
plt.legend()
plt.show()
	

# selection(arr1)
# insertion(arr2)
