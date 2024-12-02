class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        self.points = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, name):
        if name == "player1":
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def get_score(self):
        if self.score1 == self.score2:
            return self.draw_game()
        if self.score1 >= 4 or self.score2 >=4:
            return self.current_score()
        else:
            score1 = self.points[self.score1]
            score2 = self.points[self.score2]
            score = f"{score1}-{score2}"
            
        return score
 
    def draw_game(self):
        if self.score1 < 4:
            result = self.points[self.score1]
            score = f"{result}-All"
        else:
            score = "Deuce"

        return score

    def current_score(self):
        difference = self.score1 - self.score2

        if difference == 1:
            score = "Advantage player1"
        elif difference == -1:
            score = "Advantage player2"
        elif difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"

        return score