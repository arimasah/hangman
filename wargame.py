class Card():

    marks = ("♤", "♡", "♢", "♧")

    values = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

    def __init__(self, m, v):
        self.mark = m
        self.value = v

    def __lt__(self, c2):
        if self.value < c2.value:
            return True

        if self.value == c2.value:
            return self.mark < c2.mark

        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True

        if self.value == c2.value:
            return self.mark > c2.mark

        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.marks[self.mark]
        return str(v)

c1 = Card(0, 13)
c2 = Card(1, 12)
print("c1 is ", c1)
print("c2 is ", c2)
print(c1, " < " , c2, " is ", c1 < c2)
print(c1, " > " , c2, " is ", c1 > c2)

from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(j, i))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

my_deck = Deck()
for card in my_deck.cards:
    print(card)

class Player:
    def __init__(self, name):
       self.wins = 0
       self.card = None
       self.name = name

    def __repr__(self):
       return self.name

class Game:
    def __init__(self):
        p1 = input("プレイヤー１の名前を入れて！＞")
        p2 = input("プレイヤー２の名前を入れて！＞")
        self.deck = Deck()
        self.p1 = Player(p1)
        self.p2 = Player(p2)

    def print_winner(self, winner):
        print(f"{winner}の勝ちだす！！")

    def draw(self, p1n, p1c, p2n, p2c):
        print(f"{p1n}のカードは{p1c} 、{p2n}のカードは{p2c} Death!!")

    def game_start(self):
        cards = self.deck.cards
        print("さあ、戦争を始めましょう！！\n Ace > King > Queen >...>2 の数字で勝負が付かなければ、\n♤ >♡ >♢ >♧　での勝負になります！")
        while len(cards) >= 2:
            key_res = input("中止するには半角小文字のq、続けるにはそれ以外の文字を入れてEnterじゃ！")
            if key_res == "q":
                break
            p1c = self.deck.draw()
            p2c = self.deck.draw()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.print_winner(self.p1.name)
            else:
                self.p2.wins += 1
                self.print_winner(self.p2.name)
        print(f"カードがなくなったの。。{self.p1.name}は{self.p1.wins}勝ち、{self.p2.name}は{self.p2.wins}勝ったの")
        print(self.winner(self.p1, self.p2))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name + "の総合優勝じゃ！！"
        if p1.wins < p2.wins:
            return p2.name + "の総合優勝じゃ！！"
        else:
            return "引き分けじゃな。つまらん。。"

game = Game()
game.game_start()
