#Don Baker
#Lab 2, Problem 3

#Write a python program to create any one of the following management systems.
#You can also pick one of your own.
#a. Library Management System (should have classes for Person, Student, Librarian, Book etc.)
#b. Airline Booking Reservation System (classes for Flight,Person,Employee,Passenger etc.)
#c. Hotel Reservation System (classes for Room,Occupants,Employee etc.)
#d. Student Enrollment System (classes for Student,System,Grades etc.)
#e. Expense Tracker System (classes for Expense, Transaction Category etc.)

#Prerequisites:
#Your code should have at least five classes.
#Your code should have _init_ constructor in all the classes
#Your code should show inheritance atleast once
#Your code should have one super call
#Use of self is required
#Use at least one private data member in your code.
#Use multiple Inheritance atleast once
#Create instances of all classes and show the relationship between them.
#Your submission code should point out where all these things are present.


#Create the Python code for a levee inspection system

#Create class for Levee
class Levee:

    #Create constructor for Levee class
    def __init__(self,name,location):
        self.levee_name = name
        self.levee_location=location

#Create class for levee systems
class Levee_System:

    #Create constructor for Levee class
    def __init__(self, syst_name,syst_location):
        self.system_name = syst_name
        self.system_location=syst_location


#Create class for levee owners
class Owner(Levee):
    pass

    #Create constructor for Levee owner
    def __init__(self,owner,name,location):
        self.system_owner=owner
        self.levee_name = name
        self.levee_location = location

#Create class for levee construction era
class Construction_Era(Levee_System):
    pass

    # Create constructor for construction era
    def __init__(self,era,syst_name,syst_location):
        self.const_era=era
        self.system_name = syst_name
        self.system_location = syst_location

#Create class for levee condition
class Condition(Levee):
    pass

    # Create constructor for levee condition
    def __init__(self, condition,name,location):
        super().__init__(name,location)  # Super call Levee
        self.levee_condition = condition
        self.levee_name = name
        self.levee_location = location

#Create class for levee repair cost range
class Repair_Cost(Levee, Levee_System): #Multiple inheritance
    pass

    #Create constructor for repair cost of levee
    def __init__(self, cost,name,location,syst_name,syst_location):
        self.levee_cost=cost
        self.levee_name = name
        self.levee_location = location
        self.system_name = syst_name
        self.system_location = syst_location

#Define the levees for class Levee
Levee1=Levee("MR361","Holt County")
Levee2=Levee("ML256","Chase County")
Levee3=Levee("ML457","Gray County")

#Define levee system
LeveeSys1=Levee_System("Missouri River Right Bank","Nebraska")
LeveeSys2=Levee_System("Missouri River Left Bank","Missouri")

#Define Owners
Own1=Owner("USACE","MR361","Holt County")
Own2=Owner("ML Levee District","ML256","Chase County")
Own3=Owner("Levee District 1","ML457","Gray County")

#Define Eras
Era1=Construction_Era("1950","Missouri River Right Bank","Nebraska")
Era2=Construction_Era("1960","Missouri River Left Bank","Missouri")

#Define Condition
Cond1=Condition("Good","MR361","Holt County")
Cond2=Condition("Fair","ML256","Chase County")
Cond3=Condition("Poor","ML457","Gray County")

#Define Costs
Cost1=Repair_Cost("$100,000","MR361","Holt County","Missouri River Right Bank","Nebraska")
Cost2=Repair_Cost("$200,000","ML256","Chase County","Missouri River Left Bank","Missouri")
Cost3=Repair_Cost("$300,000","ML457","Gray County","Missouri River Left Bank","Missouri")

#print(Levee1)

print("The leveee name for Levee 1 is:",Levee1.levee_name)
print("The location for levee system 1 is:",LeveeSys1.system_location)
print("The owner for levee system 1 is",Own1.system_owner)
print("Levee system 2 was constructed in:",Era2.const_era)
print("The condition of levee 2 is:",Cond2.levee_condition)
print("The repair cost for levee 3 is:",Cost3.levee_cost)