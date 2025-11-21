# Dictionary in Python

'''
Dictionaries are used to store data values in key:value pairs “key” : value
They are unordered, mutable(changeable) & don’t allow duplicate keys

Example: 
dict={
   "name": "khushi",
    "CGPA": 9.6,
    "marks": [98,97,95],
}                                 
dict["name"],dict["CGPA"],dict["marks"]
dict["key"]="value" #to assign or add new 

'''

Dict= {
    "SName" : "khushi",
    "FName" : "Praveen Nigam",
    "RollNO.": 101,
    "Stream": "PCM",
    "Category": "Genral",
    "Blind": False,  
}

# Function for Dist 
print(Dict["Blind"])
print(Dict.keys())
print(Dict.values())
print(Dict.items())
print(Dict.get("Category"))
print(Dict.update({"Blind":"True"}))
print(Dict["Blind"])






