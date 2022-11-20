import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Diamonds", 5)
        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        is_ace = self.card_game.check_for_ace(self.card1)
        self.assertEqual(True, is_ace)

    def test_highest_card(self):
        highest_card = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, highest_card)

    def test_cards_total(self):
        card_total = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 6", card_total)