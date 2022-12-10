# first_name = "Zen"
# last_name = "Coder"
# age = 28
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# #another way to print the following using .format()
# print("My name is {} {} and I am {} years old.".format(first_name, last_name,age))

first_name = "Alana"
last_name = "Da Silva"
age = 36
profession = "Software Developer"
years_experience = 5

greeting = "Hello my name is {} {}"

print(greeting.format(first_name, last_name)) 
# Desired output: Hello my name is Alana Da Silva

print(f"I am {age} years old") 
# Desired output: I am 36 years old

print("I work as a {}.".format(profession))
# Desired output: I work as a Software Developer.

exp_string = "I have worked in the field for {} years."
print(exp_string.format(years_experience))
# Desired output: I have worked in the field for 5 years.

print("I started in the field when I was " + str(int(age) - int(years_experience)) + " years old.")
# Desired output: I started in the field when I was 31 years old.