#data structure
shopping_list = ['marshmallows', 'chocolate', 'crackers', 'grapes'] #list/array

index = 2
print ( shopping_list[index])

"""
    FOR LOOP
"""
for index in range(10):
    print ( index )


"""
    for ( let x = 2; x < 10; x++)    
"""
print("start and finish")
for index in range(2,10):
    print (index)

print ("steps")
for index in range(2,10,5):
    print (index)

print ("backwards")
for index in range(10,2,-1):
    print (index)

for index in range(len(shopping_list)):
    print (shopping_list[index])

some_word = "supercalifregiedicsuperlidocious"

print(len(some_word))
print(some_word[2:13]) #range
print(shopping_list[1:3])

"""
    WHILE LOOP
"""

x=1

while(x <= 10):
    print (x)
    x += 1

is_full = False
appetite = 5
eat_count = 0

while(is_full == False):
    print ("is eating")
    eat_count += 1
    if eat_count == 5:
        is_full = True

"""
SPECS
    Create a collection of items the character can carry
    Add an 'inventory' action that displayhs all the items in the inventory
"""
