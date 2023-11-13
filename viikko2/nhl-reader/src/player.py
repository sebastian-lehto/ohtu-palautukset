class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals + self.assists
        self.nationality = dict["nationality"]
    
    def __str__(self):
        ret = f"{self.name:20}" + " team " + f"{self.team:3}" + " goals " + f"{str(self.goals):3}" + " assists " + f"{str(self.assists):3}" + " points " + f"{self.points:4}"
        return ret
