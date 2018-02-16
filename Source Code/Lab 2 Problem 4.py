#Don Baker
#Lab 2

#Using Numpy create random vector of size 15 having only Integers in the range 0 - 20.
#Write a program to find the most frequent item/value in the vector list.

#Import the Numpy package
import numpy as np

#Ask the user to enter the low and high range for the random integer vector, and the size of the vector.
l=int(input("Please enter the low integer value in the range of the random vector. The lowest value allowed is zero.\n"))
h=int(input("Please enter the high integer value in the range of the random vector.\n"))
s=int(input("Please enter the size of the vector."))

#Create random vector of integers from 0 to 20
Vec = np.random.randint(l,h,s)

#Print vector
print("\nHere is the random vector.")
print(Vec)

#Find and print the most frequent integer in the random vector
most_freq=np.bincount(Vec).argmax()
print("\nThe most frequent integer in the random vector is",most_freq,".")