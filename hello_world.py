# 1. TASK: print "Hello World"
print( 'Hello World' )
# 2. print "Hello Noelle!" with the name in a variable
name = "Jackie"
print( "Hello", name )	# with a comma
print( "Hello " + name )	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 10
print( "Hello", name )	# with a comma
print( "Hello " + str(name) )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I love to eat {}".format(fave_food1) ) # with .format()
print( f"I love to eat {fave_food2}") # with an f string

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
# else:		# only executes on a clean exit from the while loop (i.e. not a break)
#    print("Final else statement")

