
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        #rewards member default value of false
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("========================")
        print(f'First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge:{self.age}\nReward Member = {self.is_rewards_member}\nGold Card Points = {self.gold_card_points}')
        print("========================")
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            self.gold_card_points = 200
            print(f'Welcome {self.first_name}! Your gold card points is: {self.gold_card_points} ')
            self.is_rewards_member = True
            return self
        else:
            print(f"{self.first_name}, You are already a member")
            
            return self
    
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print(f"Sorry {self.first_name}, You do not have enough Points to spend")
            return self
        else:
            self.gold_card_points = self.gold_card_points - amount
            print(f'{self.first_name}, You have spent {amount} points and have a remaining balance of {self.gold_card_points} points')
            return self



user1 = User("John", "O'Reily", "jor@yahoo.com", 29)
user1.display_info().enroll().spend_points(50)
user2 = User("Jaz", "O'Conner", "jazzy@gmail.com", 33)
user3 = User("Jules", "O'Farrel", "joff@hotmail.com", 23)
user2.enroll().spend_points(80).display_info()
user3.display_info().spend_points(25)
user1.enroll()
