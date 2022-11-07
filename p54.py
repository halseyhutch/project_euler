from collections import defaultdict


class Card:

    def __init__(self, card_string):
        match card_string[0]:
            case 'A': self.rank = 14
            case 'K': self.rank = 13
            case 'Q': self.rank = 12
            case 'J': self.rank = 11
            case 'T': self.rank = 10
            case _ : self.rank = int(card_string[0])
        self.suit = card_string[1]


class Hand:

    def __init__(self, hand):

        self.cards = []
        for card in hand:
            self.cards.append(Card(card))
        
        # this kind of invalidates the whole card class. oh well.
        unique_ranks = set()
        unique_suits = set()
        ranks = []
        rank_counts = defaultdict(int)
        for card in self.cards:
            unique_ranks.add(card.rank)
            unique_suits.add(card.suit)
            ranks.append(card.rank)
            rank_counts[card.rank] += 1
        sorted_ranks = sorted(ranks)
        is_flush = len(unique_suits) == 1
        is_straight = (sorted_ranks == list(range(min(ranks), max(ranks)+1)) or
            sorted_ranks == [2, 3, 4, 5, 14])
        
        # royal flush
        if is_flush and sorted_ranks == [10, 11, 12, 13, 14]:
            self.hand_rank = 10
            self.high_card = 14
        # straight flush
        elif is_flush and is_straight:
            self.hand_rank = 9
            self.high_card = max(ranks)
        # four of a kind
        elif max(rank_counts.values()) == 4:
            self.hand_rank = 8
            keys = list(rank_counts.keys())
            values = list(rank_counts.values())
            self.high_card = keys[values.index(4)]
            self.tiebreaker = keys[values.index(1)]
        # full house
        # this check is sufficient since we already did 4 of a kind
        elif len(unique_ranks) == 2:
            self.hand_rank = 7
            keys = list(rank_counts.keys())
            values = list(rank_counts.values())
            self.high_card = keys[values.index(3)]
            self.tiebreaker = keys[values.index(2)]
        # flush
        elif is_flush:
            self.hand_rank = 6
            self.high_card = max(ranks)
        # straight
        elif is_straight:
            self.hand_rank = 5
            self.high_card = max(ranks)
        # three of a kind
        # again, relies on checking for full house beforehand.
        # this reliance continues further down
        elif max(rank_counts.values()) == 3:
            self.hand_rank = 4
            keys = list(rank_counts.keys())
            values = list(rank_counts.values())
            self.high_card = keys[values.index(3)]
            self.tiebreaker = max([keys[i] for i, x in enumerate(values) if x == 1])
        # two pair
        elif len(unique_ranks) == 3:
            self.hand_rank = 3
            keys = list(rank_counts.keys())
            values = list(rank_counts.values())
            self.high_card = max([keys[i] for i, x in enumerate(values) if x == 2])
            self.tiebreaker = min([keys[i] for i, x in enumerate(values) if x == 2])
        # one pair
        elif len(unique_ranks) == 4:
            self.hand_rank = 2
            keys = list(rank_counts.keys())
            values = list(rank_counts.values())
            self.high_card = keys[values.index(2)]
            self.tiebreaker = max([keys[i] for i, x in enumerate(values) if x == 1])
        # high card
        else:
            self.hand_rank = 1
            self.high_card = max(ranks)


    def compare(self, other_hand):
        if self.hand_rank > other_hand.hand_rank:
            return 1
        elif self.hand_rank < other_hand.hand_rank:
            return 0
        else:
            if self.high_card > other_hand.high_card:
                return 1
            elif self.high_card < other_hand.high_card:
                return 0
            else:
                if self.tiebreaker > other_hand.tiebreaker:
                    return 1
                # don't need to go beyond this level for this data set.
                else:
                    return 0


def p54():
    with open('data/p54.txt') as f:
        hands_data = f.read().split('\n')
    res = 0
    for hands in hands_data:
        hands = hands.split()
        h1 = Hand(hands[:5])
        h2 = Hand(hands[5:])
        res += h1.compare(h2)
    return res


print(p54())