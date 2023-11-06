import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_toimii(self):
        self.p1 = self.stats.search("Kurri")
        self.assertAlmostEqual(self.p1.name, "Kurri")

    def test_search_toimii_vaaralla_haulla(self):
        self.p1 = self.stats.search("Kuuuurrrrri")
        self.assertAlmostEqual(self.p1, None)

    def test_team_toimii(self):
        self.t1 = self.stats.team("PIT")
        self.assertAlmostEqual(self.t1[0].name, "Lemieux")

    def test_top_points_toimii(self):
        self.p1 = self.stats.top(1, SortBy.POINTS)[0]
        self.assertAlmostEqual(self.p1.name, "Gretzky")
    
    def test_top_goals_toimii_1(self):
        self.p1 = self.stats.top(2, SortBy.GOALS)[0]
        self.assertEqual(self.p1.name, "Lemieux")
    
    def test_top_goals_toimii_2(self):
        self.p1 = self.stats.top(2, SortBy.GOALS)[1]
        self.assertEqual(self.p1.name, "Yzerman")

    def test_top_assists_toimii(self):
        self.p1 = self.stats.top(1, SortBy.ASSISTS)[0]
        self.assertAlmostEqual(self.p1.name, "Gretzky")