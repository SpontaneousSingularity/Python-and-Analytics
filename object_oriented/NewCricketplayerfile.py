from playerFile import Player
#cricket player-> derived class

class CricketPlayer(Player):

    def __init__(self,first_name,last_name,birth_year,):
        super().__init__(first_name,last_name,birth_year)
        self.scores = []

    def add_score(self,score):
        self.scores.append(score)

    def findAverage(self):
        return round(sum(self.scores)/len(self.scores),2)

    def __str__(self):
        return f"{super().__str__()+f"Scores: {self.scores}\nAverage Score: {self.findAverage()}"}"
    
    #Operator overloading
    def __lt__(self,other):
        self_average_score = self.findAverage()
        other_average_score = other.findAverage()

        return self_average_score < other_average_score
    
    def __le__(self,other):
        self_average_score = self.findAverage()
        other_average_score = other.findAverage()

        return self_average_score <= other_average_score
    
    def __ge__(self,other):
        self_average_score = self.findAverage()
        other_average_score = other.findAverage()

        return self_average_score >= other_average_score