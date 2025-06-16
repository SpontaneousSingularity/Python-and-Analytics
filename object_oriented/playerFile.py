#pascalcase
import datetime as dt 

class Player:

    def __init__(self,first_name,last_name,birth_year):
        print("Object of player created")
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def get_age(self):
        current_year = dt.datetime.now().year
        return current_year - self.birth_year
    
    def __str__(self):
        return f"~~PLayer Info~~]\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nBirth Year: {self.birth_year}\nAge: {self.get_age()}"