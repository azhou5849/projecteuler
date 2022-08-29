"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives.
But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared; if the highest cards tie then the next highest cards are compared, and so on.
The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
How many hands does Player 1 win?
"""
rank_chars = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
type_order = [  "High Card",
                "One Pair",
                "Two Pairs",
                "Three of a Kind",
                "Straight",
                "Flush",
                "Full House",
                "Four of a Kind",
                "Straight Flush",
                "Royal Flush"  ]

class Card:
    """
    Ranks are stored as ints from 2 through 14 (J = 11, Q = 12, K = 13, A = 14)
    Suits are stored as characters from ['C', 'D', 'H', 'S']
    Cards are totally ordered, with suits being ordered alphabetically (but Hands will not be)
    """
    def __init__(self, card_str):  # card_str is a string of two characters, first rank then suit
        self.rank = rank_chars[card_str[0]]
        self.suit = card_str[1]

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        elif self.rank == other.rank:
            return self.suit < other.suit
        else:
            return False

    def __le__(self, other):
        if self.rank < other.rank:
            return True
        elif self.rank == other.rank:
            return self.suit <= other.suit
        else:
            return False


class Hand:
    def __init__(self, card_list = []):
        self.card_list = card_list

    def add_card(self, card):
        self.card_list.append(card)
        self.card_list.sort()

    def evaluate(self):
        if len(self.card_list) != 5:
            raise Exception("Something went wrong")
        is_flush = True
        for c in self.card_list:
            if c.suit != c[0].suit:
                is_flush = False
        if is_flush:
            ranks = [c.rank for c in self.card_list]  # this should already be sorted
            if ranks[4] - ranks[0] == 4:
                if ranks[0] == 10:
                    self.type = "Royal Flush"
                else:
                    self.type = "Straight Flush"
                    self.tiebreak = ranks[0]
            else:
                self.type = "Flush"
                self.tiebreak = ranks
        else:
            unique_ranks = []
            for c in self.card_list:
                if c.rank not in unique_ranks:
                    unique_ranks.append(c.rank)  # this should already be sorted from top to bottom
            if len(unique_ranks) == 2:  # split is either 4-1 or 3-2
                if unique_ranks[0] < unique_ranks[1] or unique_ranks[3] < unique_ranks[4]:
                    self.type = "Four of a Kind"
                else:
                    self.type = "Full House"
            elif len(unique_ranks) == 3:
                if



    @classmethod
    def read_hands(cls, line):
        """
        Returns a Hand pair read from a line of the file
        """
        card_strs = line.split()
        first_hand, second_hand = Hand([]), Hand([])
        for i in range(10):
            if i < 5:
                first_hand.add_card(Card(card_strs[i]))
            else:
                second_hand.add_card(Card(card_strs[i]))
        return first_hand, second_hand

with open("p0054poker.txt", 'r') as f:
    line = f.readline()
    first_hand, second_hand = Hand.read_hands(line)
