from playerFile import Player
#pascalCase
import datetime as dt

class TennisPlayer(Player):

    #constructor
    def __init__(self,first_name,last_name,birth_year):
        super().__init__(first_name,last_name,birth_year)
        print("object of TennisPlayer created")
        self.aces = []

        #Methods
        def add_ace_score(self,ace):
            self.aces.append(ace)

        def findAverage(self):
            return round(sum(self.aces)/len(self.aces),2)
        
    def __str__(self):
        return super().__str__() +f"Aces: {self.aces}\nAverage Aces: {self.findAverage()}"  