from player_reader import PlayerReader

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nat):
        natPlayers = list(filter(lambda x: x.nationality == "FIN", self.players))
        natPlayers.sort(key = lambda e: e.points, reverse=True)
        return natPlayers