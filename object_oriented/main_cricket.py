from NewCricketplayerfile import CricketPlayer

virat = CricketPlayer("Virat","Kohli",1988)

virat.add_score(100)
virat.add_score(200)
virat.add_score(50)
virat.add_score(75)

print (virat)

david = CricketPlayer("David","Warner",1986)

david.add_score(100)
david.add_score(200)
david.add_score(50)
david.add_score(75)

print(david)

print(virat<david)
print(virat>david)
print(david <= +virat)
print(david>=virat)
