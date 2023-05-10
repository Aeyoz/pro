from __future__ import annotations


def load_card_glyphs(path: str = 'cards.dat') -> dict[str, str]:
    '''Retorna un diccionario donde las claves serán los palos
    y los valores serán cadenas de texto con los glifos de las
    cartas sin ningún separador'''
    with open(path) as f:
        new_deck = {}
        for line in f:
            suit, cards = line.replace(",","").strip("\n").split(":")
            new_deck[suit] = cards
        return new_deck


class Card:
    CLUBS = '♣'
    DIAMONDS = '◆'
    HEARTS = '❤'
    SPADES = '♠'
    SUITS = (CLUBS, DIAMONDS, HEARTS, SPADES)
    #           1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    K_VALUE = 13
    GLYPHS = load_card_glyphs()

    def __init__(self, value: int | str, suit: str):
        '''Notas:
        - Si el suit(palo) no es válido hay que elevar una excepción de tipo
        InvalidCardError() con el mensaje: 🃏 Invalid card: {repr(suit)} is not a supported suit
        - Si el value(como entero) no es válido (es menor que 1 o mayor que 13) hay que
        elevar una excepción de tipo InvalidCardError() con el mensaje:
        🃏 Invalid card: {repr(value)} is not a supported value
        - Si el value(como string) no es válido hay que elevar una excepción de tipo
        🃏 Invalid card: {repr(value)} is not a supported symbol

        - self.suit deberá almacenar el palo de la carta '♣◆❤♠'.
        - self.value deberá almacenar el valor de la carta (1-13)'''
        if suit not in Card.SUITS:
            raise InvalidCardError(f": {repr(suit)} is not a supported suit")
        if isinstance(value, int):
            if value < Card.A_VALUE or value > Card.K_VALUE:
                raise InvalidCardError(f": {repr(value)} is not a supported value")
        elif isinstance(value, str):
            if value.upper() not in Card.SYMBOLS:
                raise InvalidCardError(f": {repr(value)} is not a supported symbol")
        self.suit = suit
        try:
            self.value = Card.SYMBOLS.index(value) + 1
        except ValueError:
            self.value = value

    @property
    def cmp_value(self) -> int:
        '''Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS.'''
        return Card.A_VALUE + Card.K_VALUE if self.value == Card.A_VALUE else self.value

    def __repr__(self):
        '''Devuelve el glifo de la carta'''
        return Card.GLYPHS[self.suit][self.value - 1]

    def __eq__(self, other: Card | object):
        '''Indica si dos cartas son iguales'''
        return self.suit == other.suit and self.value == other.value

    def __lt__(self, other: Card):
        '''Indica si una carta vale menos que otra'''
        return self.cmp_value < other.cmp_value

    def __gt__(self, other: Card):
        '''Indica si una carta vale más que otra'''
        return self.cmp_value > other.cmp_value

    def __add__(self, other: Card) -> Card:
        '''Suma de dos cartas:
        1. El nuevo palo será el de la carta más alta.
        2. El nuevo valor será la suma de los valores de las cartas. Si valor pasa
        de 13 se convertirá en un AS.'''
        new_suit = self.suit if self.cmp_value > other.cmp_value else other.suit
        comparison_value = self.cmp_value + other.cmp_value
        new_value = comparison_value if comparison_value < Card.K_VALUE else Card.A_VALUE
        return Card(new_value, new_suit)

    def is_ace(self) -> bool:
        '''Indica si una carta es un AS'''
        return self.value == Card.A_VALUE

    @classmethod
    def get_available_suits(cls) -> str:
        '''Devuelve todos los palos como una cadena de texto'''
        return "".join(Card.GLYPHS)

    @classmethod
    def get_cards_by_suit(cls, suit: str):
        '''Función generadora que devuelve los glifos de las cartas por su palo'''
        for card in Card.GLYPHS[suit]:
            yield card


class InvalidCardError(Exception):
    '''Clase que representa un error de carta inválida.
    - El mensaje por defecto de esta excepción debe ser: 🃏 Invalid card
    - Si se añaden otros mensajes aparecerán como: 🃏 Invalid card: El mensaje que sea'''
    def __init__(self, message=""):
        self.message = message
        super().__init__(message)
        self.header = "🃏 Invalid card"
    
    def __str__(self):
        return f"{self.header}{self.message}"

pepe = Card("K", "❤")
print(pepe)
