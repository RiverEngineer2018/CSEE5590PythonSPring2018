#Lab 1, Question 2
#Program that accepts sentence entry from user and finds middle word(s), longest word and reverses the sentence.

#Enter Sentence
Sentence=input("Please enter a sentence. Please omit punctuation.\n")

#Split sentence into a word list
Words=Sentence.split()

#Determine the middle word(s)
#Detemine middle position of the list
x=len(Words)

#Middle point of string
MidPosition=x/2

#Determine if number of words is even or odd based on remainder
Mod=int(x%2)

#Print middle words in the sentence based on even or odd number
#Even number of words
if (Mod==0):
    MidPoint=int(MidPosition-1)
    MidPoint1=MidPoint+2
    print("The middle words are: ",Words[MidPoint],", ",Words[MidPoint1],".")

#Odd number of words.
else:
    MidPoint=int(MidPosition+0.5)
    print("The middle word is ",Words[MidPoint],".")

#Determine longest word in sentence.

#Sort words based on length
SortedWords = sorted(Words, key=len)

#Print the longest word which is the last one in the list.
print("The longest word in the list is: %s.\n" % (SortedWords[-1],))

#Print the sentence with words in reverse order.
print("The sentence with words in reverse order is: ",Sentence[::-1])


