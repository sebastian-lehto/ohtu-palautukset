class TennisGame:
    def __init__(self, p1_name, p2_name):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_score = 0
        self.p2_score = 0
        self.score_transaltions = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score = self.p1_score + 1
        else:
            self.p2_score = self.p2_score + 1

    def get_score(self):
        score = ""
        score_difference = self.p1_score - self. p2_score

        if score_difference == 0:
            score = self.get_even_score(self.p1_score)
        
        elif self.p1_score >= 4 or self.p2_score >= 4:
            score = self.get_advantage(score_difference)
        else:
            score = self.get_regular_score()

        return score

    def get_even_score(self, score):
        if score < 4:
            return f'{self.score_transaltions[score]}-All'
        else:
            return "Deuce"

    def get_regular_score(self):
        return f'{self.score_transaltions[self.p1_score]}-{self.score_transaltions[self.p2_score]}'

    def get_advantage(self, difference):
        if difference * difference == 1:
            return f'Advantage {self.get_leader(difference)}'

        return f'Win for {self.get_leader(difference)}'

    def get_leader(self, difference):
        return self.p1_name if difference > 0 else self.p2_name
