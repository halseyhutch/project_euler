# not a performant approach, but easy to understand

import random
from collections import Counter


SQUARES = [
    'GO',
    'A1',
    'CC1',
    'A2',
    'T1',
    'R1',
    'B1',
    'CH1',
    'B2',
    'B3',
    'JAIL',
    'C1',
    'U1',
    'C2',
    'C3',
    'R2',
    'D1',
    'CC2',
    'D2',
    'D3',
    'FP',
    'E1',
    'CH2',
    'E2',
    'E3',
    'R3',
    'F1',
    'F2',
    'U2',
    'F3',
    'G2J',
    'G1',
    'G2',
    'CC3',
    'G3',
    'R4',
    'CH3',
    'H1',
    'T2',
    'H2'
]

COMMUNITY_CHEST = [
    'GO',
    'JAIL',
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None
]

CHANCE = [
    'GO',
    'JAIL',
    'C1',
    'E3',
    'H2',
    'R1',
    'NEXT R',
    'NEXT R',
    'NEXT U',
    'BACK 3',
    None,
    None,
    None,
    None,
    None,
    None
]


def shuffle(x):
    return random.sample(x, k=len(x))


class MonopolyToken:
    def __init__(self, die_sides=6, debug=False):
        self.die_sides = die_sides
        self.square = 'GO'
        self.num_doubles = 0
        self.community_chest_deck = shuffle(COMMUNITY_CHEST)
        self.community_chest_index = 0
        self.chance_deck = shuffle(CHANCE)
        self.chance_index = 0
        self.debug = debug

    def roll_die(self):
        d1 = random.randint(1, self.die_sides)
        d2 = random.randint(1, self.die_sides)
        return d1 + d2, d1 == d2
    
    def move(self):
        # locate current position
        i = SQUARES.index(self.square)

        # roll die
        die, is_double = self.roll_die()
        if self.debug:
            print(f'Player rolls a {die}.')

        # handle doubles
        if is_double:
            self.num_doubles += 1
            if self.debug:
                print(f'This is a double! Double count at {self.num_doubles}.')
            if self.num_doubles == 3:
                # assume we immediately pay to get out of jail
                self.square = 'JAIL'
                self.num_doubles = 0
                return
        else:
            self.num_doubles = 0
        
        # move to new square
        i = (i + die) % len(SQUARES)
        self.square = SQUARES[i]
        if self.debug:
            print(f'Player moves to {self.square}.')

        # go to jail
        if self.square == 'G2J':
            self.square = 'JAIL'
            if self.debug:
                print(f'Go to jail! Player moves to {self.square}.')

        # community chest
        if self.square in ['CC1', 'CC2', 'CC3']:
            card = self.community_chest_deck[self.community_chest_index]
            self.community_chest_index += 1
            self.community_chest_index %= len(self.community_chest_deck)
            if card is not None:
                self.square = card
            if self.debug:
                print(f'Community Chest! Player moves to {self.square}.')
        
        # chance
        if self.square in ['CH1', 'CH2', 'CH3']:
            card = self.chance_deck[self.chance_index]
            self.chance_index += 1
            self.chance_index %= len(self.chance_deck)
            if card == 'BACK 3':
                self.square = SQUARES[i - 3]
            elif card == 'NEXT R':
                if self.square == 'CH1':
                    self.square = 'R2'
                elif self.square == 'CH2':
                    self.square = 'R3'
                elif self.square == 'CH3':
                    self.square = 'R1'
            elif card == 'NEXT U':
                if self.square == 'CH1':
                    self.square = 'U1'
                elif self.square == 'CH2':
                    self.square = 'U2'
                elif self.square == 'CH3':
                    self.square = 'U1'
            elif card is not None:
                self.square = card
            if self.debug:
                print(f'Chance! Player moves to {self.square}.')


def p84(die_sides=6, sample_size=100000):
    token = MonopolyToken(die_sides=die_sides)
    squares = []
    for _ in range(sample_size):
        token.move()
        squares.append(token.square)
    most_common = Counter(squares).most_common(3)
    print(most_common)
    return ''.join([str(SQUARES.index(k)) for k, _ in most_common])


if __name__ == '__main__':
    print(p84(die_sides=4, sample_size=1_000_000))
