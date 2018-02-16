#Don Baker
#Lab 2, Problem 2

#With any given mobile phone number n, there is contact list.
#Create a list of contacts and then prompt the user to do the following:
#a) Display contact by name
#b) Display contact by number
#c) Edit contact by name
#d) Exit

#Define the Print Instructions routine for the user
def PrintInstructions():
    print("Please choose one of the following choices: ")
    print("1 - Display contact by name")
    print("2 - Display contact by number")
    print("3 - Edit phone number by contact name")
    print("4 - Exit\n")

#Main program
def main():

#Create contact list
    contact_list = [{"name": "Rashmi", "number": "8797989821", "email": "rr@gmail.com"},
                    {"name": "Saria", "number": "9897989821", "email": "ss@gmail.com"}]

#print the instructions for the user
    PrintInstructions()

#Input the users choice
    choice = int(input("Enter choice: "))

    while choice != 4:

#Retrieve contact by name
        if choice == 1:
            name = input("Please enter contact name to be retrieved: ")
            print()
            for dic in contact_list:
                if ("name", name) in dic.items():
                    for k, v in dic.items():
                        print(k, ":", v)

#Retrieve contact by number
        if choice == 2:
            number = input("Please enter contact number to be retrieved: ")
            print()
            for dic in contact_list:
                if ("number", number) in dic.items():
                    for k, v in dic.items():
                        print(k, ":", v)

#Change phone mumber by entering name of contact
        if choice == 3:
            name = input("Enter contact name to change: ")
            newNumber = input("Enter new number: ")
            print()

            for dic in contact_list:
                if ("name", name) in dic.items():
                    dic["number"] = newNumber
                    for k, v in dic.items():
                        print(k, ":", v)

        choice = int(input("\nEnter choice: "))


if __name__ == "__main__":
    main()