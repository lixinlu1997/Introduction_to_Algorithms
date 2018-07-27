import numpy as np
import random

def insertion_sort(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j - 1
		while  i >=  0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key
	return A 

def main():
	A = np.random.randint(0,100,20)
	print("The origin list is:")
	print(A.tolist())
	A = insertion_sort(A)
	print("After insertion sort:")
	print(A.tolist())

if __name__ == '__main__':
	main()
		
	
