from player import Player
from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [player for player in self.players if player.nationality == nationality]


        sorted_players = sorted(filtered_players, key=lambda player: player.all_points(), reverse=True)

        return sorted_players