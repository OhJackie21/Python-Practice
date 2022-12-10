# Basic - Print all integers from 0 to 150.
for x in range(0, 151):
    print(x)

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for y in range( 5, 1000, 5 ):
    print(y)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for j in range ( 1, 101):
    if j % 5 == 0 and j % 10 != 0:
        print( 'Coding' )
    if j % 10 == 0:
        print( 'Coding Dojo' )
    else:
        print(j)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
add = 0
for k in range( 0, 500000):
    if k % 2 != 0:
        add = add + k
print(add)

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for l in range ( 2018, 0, -4 ):
    print(l)

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 7
highNum = 43
mult = 7

for m in range( lowNum, highNum, mult):
    print(m)