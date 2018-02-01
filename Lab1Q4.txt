#Program to compare the students in two lists

#Students in Python list
Python=["Donald","Kelli","Jack","Roger","Kim","Shelly","Paul"]

#Students in Web Application list
WebApplication=["Jon","Paul","Lisa","Pam","Roger","Kelli","Jane","Bob"]

#Print list of students in Python class.
print("The students in the Python class are:")
print(Python)
print()

#Print list of students in Web Application class.
print("The students in the Web Application class are:")
print(WebApplication)
print()

#Length of lists
PythonLength=int(len(Python))
WebAppLength=int(len(WebApplication))

#Define common and uncommon student lists
Common = []
Uncommon = []

#Define counter
z=0

#Define temporary lists
PythonTemp=[]
WebAppTemp=[]

#Loop to compare lists
for x in range (0,PythonLength):
    for y in range (0,WebAppLength):
        if Python[x]==WebApplication[y]:
            Common.append([Python[x]])


#Create list of uncommon students
#Compare lists using list comprehension
UncommonPython=[w for w in Python if w not in WebApplication]
UncommonWebApp=[z for z in WebApplication if z not in Python]

Uncommon = UncommonPython + UncommonWebApp

print("The common students between both classes are:")
print(Common)
print()

print("The students that are uncommon between the two classes are:")
print(Uncommon)