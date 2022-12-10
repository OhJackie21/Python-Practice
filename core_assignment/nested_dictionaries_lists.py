# 1.Update Values in Dictionaries and Lists
"""
Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].✔️
Change the last_name of the first student from 'Jordan' to 'Bryant'✔️
In the sports_directory, change 'Messi' to 'Andres'✔️
Change the value 20 in z to 30 ✔️

"""

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory['soccer'][0] = "Andres"
z[0]['y'] = 30

#2. Iterate Through a List of Dictionaries
"""
Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
"""
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'}, # index 0
         {'first_name' : 'John', 'last_name' : 'Rosales'}, # index 1
         {'first_name' : 'Mark', 'last_name' : 'Guillen'}, # index 2
         {'first_name' : 'KB', 'last_name' : 'Tonel'} # index 3
    ]


def iterateDictionary(some_list):
  for i in range(len(some_list)):
    fkey = students[i]['first_name']
    fval = students[i]['last_name']
    print("first_name", " = ", fkey, ",", " last_name" " = ", fval)
    
iterateDictionary(students) 

"""
ANOTHER WAY OF DOING THIS, BUT MUCH EASIER

def iterate_dictionary(list):
    for i in range(0, len(list)):
        output = ""
        for key,val in list[i].items():
            output += f" {key} - {val},"
        print(output)
"""

#3. Get Values From a List of Dictionaries
"""
    Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
    Michael
    John
    Mark
    KB

    And iterateDictionary2('last_name', students) should output:
    Jordan
    Rosales
    Guillen
    Tonel

"""

def iterateDictionary2(key_name, some_list):
  for i in range(len(students)):
    for keyN, valN in some_list[i].items():
      if keyN == key_name:
        print(valN)


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


#4. Iterate Through a Dictionary with List Values
"""
   Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

"""


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    #^^ this is keyLoc 
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
                    # ^^ these are the valInst and are a list
}

def printInfo(some_dict):
  for keyLoc, valInst in dojo.items():
    print("_______________")
    print(f"{len(valInst)} {keyLoc}")
    for i in range(len(valInst)):
      print(valInst[i])
    print("_______________")
printInfo(dojo)