import numpy as np
import random
import sys

def insertion_sort(A,mode):
	for j in range(1,len(A)):
		key = A[j]
		i = j - 1
		if mode == str(1):
			while i >= 0 and A[i] > key:
				A[i+1] = A[i]
				i -= 1
		elif mode == str(2):
			while i >= 0 and A[i] < key:
				A[i+1] = A[i]
				i -= 1
		A[i+1] = key
	return A 

def main(mode):
	A = np.random.randint(0,100,20)
	print("The origin list is:")
	print(A.tolist())
	A = insertion_sort(A,mode)
	print("After insertion sort:")
	print(A.tolist())

if __name__ == '__main__':
	if len(sys.argv) != 2 :
		print("Please input mode, 1 is conscending, 2 is descending")
		assert(0)
	if sys.argv[1] != str(1) and sys.argv[1] != str(2):
		print("Please input correct mode!")
		assert(0)
	main(sys.argv[1])
		
	
