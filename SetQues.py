'''
Q.1 Store following word meanings in a python dictionary:

table : “a piece of furniture”,“list of facts & figures”
cat : “a small animal”

'''
# Solution 
Dictionary={
    "table" : ["a piece of furniture","list of facts & figures"], #list
    "cat" : "a small animal",
}

print(Dictionary)
print(Dictionary["table"])
print(Dictionary["cat"])

'''
Que2. You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.


”python”,“java”,“C++”,“python”,“javascript”,
“java”,“python”,“java”,“C++”,“C”

'''
# Solution
Set={
    "python","java","C++","python","javascript",
     "java","python","java","C++","C"
     }
print(Set)
print(len(Set))

'''
Question 3. WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value.
'''
# Solution 
Dictionary={}
PhyMark =input("Enter the Phy marks: ")
Dictionary.update({"Phy": PhyMark })

ChemMark =input("Enter the Chem Makrs: ")
Dictionary.update({"Chem": ChemMark })

MathsMark =input("Enter the Maths marks: ") 
Dictionary.update({"Maths": MathsMark})

print(Dictionary)

'''
Question 4. Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)
'''
# Solution 
Set={9,"9.0"} # 9 as a int and 9.0 as a String
print(Set)
Set={"9",9.0} # 9 as a string 9.0 as int 
print(Set)

Set={
    ("Float",9,0),
    ("int", 9)
}
print(Set)



