# class User:
#     def __init__(self, fName, lName, age ):
#         self.fName = fName
#         self.lName = lName
#         self.age = age
    
#     def greeting(self):
#         print(f'Hello! My name is {self.fName} {self.lName} and I am {self.age} years old')

# oh = User("Jamie", "Oh", 25)
# love = User('Lovely', 'Jones', 65)
# oh.greeting()
# love.greeting()


class shoe:
    #now our method has 4 parameters (incuding self)!
    def __init__(self, brand, shoe_type, price):
        #we assign them accordingly
        self.brand = brand
        self.shoe_type = shoe_type
        self.price = price
        #the status is set to True by default
        self.in_stock = True
    
    def on_sale_by_percent(self, percent):
        self.price = self.price * (1 - percent)

skater_shoe = shoe("vans", "Low-Top Trainers", 59.99)
dress_shoe = shoe("Jack & Jill Bootery", "Ballet Flast", 29.99)
print(skater_shoe.price)

skater_shoe.on_sale_by_percent(0.2)
dress_shoe.on_sale_by_percent(0.5)
print(dress_shoe.price)


#replacing the whole thing below with something else
# #the skater shoes go on sale by 20% reduced price:
# skater_shoe.price = skater_shoe.price * (1 - 0.2) 

# #the Dress shoes go on sale by 10% reduction
# dress_shoe.price = dress_shoe.price * (1 - 0.1)

# #the skater shoes go on sale AGAIN by another 10%
# skater_shoe.price = skater_shoe.price * (1 - 0.1)
