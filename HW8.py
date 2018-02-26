import numpy as np
import matplotlib.pyplot as plt
import time

#this code runs by itself provided the composite_list.txt file is in the same folder
#just use run HW8.py

#---------------------------------------------------------------------------------

def primeFactor(n):
	factors = []

	#this loop will reduce any even numbers down to odd while appending each instance of 2
	#needed to reduce the number. (shouldn't need for the list provided, but still included)
	while n % 2 == 0:
	  factors.append(2)
	  n /= 2
		
	#after factoring out all the 2's, this loop will start at three and iterate through
	#the loop with all odd numbers up until the square root of the the number.
	f = 3
	while n > f**2:
	  quotient, remainder = divmod(n,f) #return quotient and remainder
	  if remainder == 0: #this means we found a factor so append to list
	    factors.append(f)
	    n = quotient #reassign n to repeat loop with new quotient
	  else:
	    f += 2 #go to next odd

	#this final condition adds the remainder after all operations have concluded
	#for example if the given number is itself a prime number
	if n != 1:
	  factors.append(n)
	return factors

def averageCalculator(d,data):
	counter = 0
	start = time.time() #for timing each runthrough
	for i in data:
		if digitCounter(i) < d: #number of digits is less than what we want to analyze, so continue
			continue
		#this exits function after digits exceeds current expected amount
		elif digitCounter(i) > d:	#the number of digits is greater than what we want so return
			elapsed = time.time() - start
			return elapsed/counter
		counter += 1 #to count number of integers successfully factored

		#call function
		prime = primeFactor(i)

		#uncommenting the line below will print out the integer and its factorization if desired
		print i," : ",prime 

def digitCounter(n):
	return len(str(int(n)))

#---------------------------------------------------------------------------------

#read in the data
composites = np.genfromtxt('composite_list.txt')

#starting from the beginning until 20-digit integers
for i in range(digitCounter(composites[0]),21):
	avg = averageCalculator(i,composites)
	print "Average time to factor ", i, " digits: ",avg, " seconds"

#---------------------------------------------------------------------------------


