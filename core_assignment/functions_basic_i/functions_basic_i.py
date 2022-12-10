#1
#prediction: 5
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#printed out 5


#2
#prediction: will have undefined
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#printed: name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined

#3
#prediction: will return 10
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#printed: 5


#4
#prediction: 10
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#printed: 5

#5
#prediction: 5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#printed: 5
#printed: NONE

#6
#prediction: 8
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#printed 3
#printed 5
#unsupported operand type(s)


#7
#prediction: 2,5
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#printed: 25


#8
#prediction: NONE
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#printed: 100
#printed: 10


#9
#prediction1: 7
#prediction2: 14
#prediction3: 21
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#printed1: 7
#printed2: 14
#printed3: 21

#10
#prediction: 8
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#printed: 8


#11
#prediction: 500
#prediction: 500
#prediction: 300
#prediction: 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#printed: 500
#printed: 500
#printed: 300
#printed: 500


#12
#prediction: 500
#prediction: 500
#prediction: 300
#prediction: 500
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#printed: 500
#printed: 500
#printed: 300
#printed: 500


#13
#prediction: 500
#prediction: 500
#prediction: 300
#prediction: 300
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#printed: 500
#printed: 500
#printed: 300
#printed: 300


#14
#prediction: 1
#prediction: 2
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#printed: 1
#printed: 3
#printed: 2


#15
#prediction: 1
#prediction: 3
#prediction: 1 , 3
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#printed: 1
#printed: 3
#printed: 5
#printed: 10