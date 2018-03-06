#Don Baker
#Comp-Sci 5590
#Lab 3, Question 3

#Take an Input file. Use the simple approach below to summarize a text file:
#-	Read the file
#-	Using Lemmatization, apply lemmatization on the words
#-	Apply the bigram on the text
#-	Calculate the word frequency (bi-gram frequency) of the words (bi-grams)
#-	Choose top five bi-grams that has been repeated most
#-	Go through the original text that you had in the file
#-	Find all the sentences with those most repeated bi-grams
#-	Extract those sentences and concatenate
#-	Enjoy the summarization


#Import Packages
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer

#Read Text File
file_path = 'd:/Google Drive/UMKC/PhD/Classes/Python/Labs/Lab 3/Python_Lab3.txt'
text_file = open(file_path,'r')
text_data=text_file.read()
text_file.close()

#Using Lemmatization, apply lemmatization on the words

#First step is to tokenize the data file into individual words
tkn = TweetTokenizer() #create a tokenizer
token = tkn.tokenize(text_data)  #tokenize the data
print("Tokenize: \n",(token),"\n")
#print(token_results)

#Now lemmatize the tokenize text file (noun is th default)
wnl = WordNetLemmatizer()  #create lemmatizer
lem = [wnl.lemmatize(tkn) for tkn in token]
print("Lemmatize (nouns): \n",lem,"\n")

#Try lemmatizing looking for verbs
wnl = WordNetLemmatizer()  #create lemmatizer
lem = [wnl.lemmatize(tkn,pos="v") for tkn in token]
print("Lemmatize (verbs): \n",lem,"\n")

#Try lemmatizing looking for adjectives
wnl = WordNetLemmatizer()  #create lemmatizer
lem = [wnl.lemmatize(tkn,pos="a") for tkn in token]
print("Lemmatize (adjectives): \n",lem,"\n")

#Try lemmatizing looking for adverbs
wnl = WordNetLemmatizer()  #create lemmatizer
lem = [wnl.lemmatize(tkn,pos="r") for tkn in token]
print("Lemmatize (adverbs): \n",lem,"\n")

#Apply bigram on the text
#Grouping two words together. This includes special characters like '('
bigram = [tkn for tkn in nltk.bigrams(token)]
print("Bigram: \n",bigram)

#Calculate the Bigram Frequency
freq_bi=nltk.FreqDist(bigram)

#Find the 5 most common bigrams
bi_common=freq_bi.most_common(5)
print("\nThe 5 most common bigrams are:\n",bi_common)