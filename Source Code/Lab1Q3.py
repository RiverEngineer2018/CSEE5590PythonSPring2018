#Lab 1, Question 3
#Program that finds triples that add to zero from a given list of integers.

#Define list.
List=[1, 3, 6, 2, -1, 2, 8, -2, 9]

#Find Triples that add to zero.

#Length of list.
Length=int(len(List))

#Loop for first set of numbers
for x in range(0,Length-3):

    #Loop for second set of numbers
    for y in range(x+1,Length-1):

        #Loop for third set of numbes
        for w in range(y+1,Length-1):
            z1=List[x]
            z2=List[y]
            z3=List[w]

            #Check to see if triples add to zero
            if (z1+z2+z3)==0:

                #Print triples
                print("[",z1,",",z2,",",z3,"]")