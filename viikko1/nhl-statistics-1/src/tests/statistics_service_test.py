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

    def test_ei_etsi_ketaan(self):
        result = self.stats.search("Unknown")
        self.assertIsNone(result)

    def test_haku(self):
        result = self.stats.search('Semenko')
        self.assertEqual(result.name, 'Semenko')

    def test_tiimi(self):
        players = self.stats.team('EDM')
        names = [player.name for player in players]
        self.assertListEqual(names, ['Semenko', 'Kurri', 'Gretzky'])

    def test_maalit(self):
        players = self.stats.top(3, SortBy.GOALS)
        names = [player.name for player in players] 
        self.assertListEqual(names, ['Lemieux', 'Yzerman', 'Kurri'])

    def test_syotot(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        names = [player.name for player in players] 
        self.assertListEqual(names, ['Gretzky', 'Yzerman', 'Lemieux'])

    def test_kaikki_pisteet(self):
        players = self.stats.top(3, SortBy.POINTS)
        names = [player.name for player in players] 
        self.assertListEqual(names, ['Gretzky', 'Lemieux', 'Yzerman'])