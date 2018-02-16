#Don Baker
#Lab 2, Problem 1

#Consider a shop UMKC with dictionary of all book items with their prices.
# Write a program to find the books from the dictionary in the range given by user.

#Create the dictionary containg the book subjects and the associated prices
books = {'Python is a Piece of Pie': 50, 'The Web is not for Spiders': 30, 'C or Sea?': 20, 'Java not Lava': 40, 'Pascal is My Pal': 10, 'Fortran Forever': 5}
print("The dictionary containing the information for books is:\n")
print(books)

#User input for price range
lr,hr = input("\nPlease the minimum and maximum price of your range you wish to pay. Please separate with a comma: ").split(',')
low_range = int(lr)
high_range = int(hr)

print("\nThe range of prices selected is $",low_range,"to $",high_range,".")

#Determine the books that fall within the selected range.

#Print the books that fall within the price range specified.
print("\nThe books that fall within the specified price range are :\n")

for key, value in books.items():
    if value >= low_range:
        if value <=high_range:
            print(key)
