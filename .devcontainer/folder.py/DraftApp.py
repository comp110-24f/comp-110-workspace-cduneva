from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.lang import Builder
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_total_rating(self):
        return sum(card['rating'] for card in self.cards)

class DraftGame(BoxLayout):
    available_cards = ListProperty([
        {"name": "LeBron James", "rating": 96},
        {"name": "Kevin Durant", "rating": 95},
        {"name": "Stephen Curry", "rating": 95},
        {"name": "Giannis Antetokounmpo", "rating": 94},
        {"name": "Kawhi Leonard", "rating": 94},
        {"name": "James Harden", "rating": 93},
        {"name": "Luka Doncic", "rating": 93},
        {"name": "Nikola Jokic", "rating": 93},
        {"name": "Joel Embiid", "rating": 92},
        {"name": "Anthony Davis", "rating": 92},
        {"name": "Damian Lillard", "rating": 91},
        {"name": "Jimmy Butler", "rating": 91},
        {"name": "Kyrie Irving", "rating": 90},
        {"name": "Paul George", "rating": 90},
    ])
    current_player = NumericProperty(1)
    current_card = StringProperty("")
    player1_cards = NumericProperty(0)
    player2_cards = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.show_next_card()

    def show_next_card(self):
        if self.available_cards:
            card = random.choice(self.available_cards)
            self.current_card = f"{card['name']} (Rating: {card['rating']})"
        else:
            self.end_game()

    def draft_card(self):
        if self.available_cards:
            card = next(c for c in self.available_cards if c['name'] in self.current_card)
            if self.current_player == 1:
                self.player1.add_card(card)
                self.player1_cards += 1
            else:
                self.player2.add_card(card)
                self.player2_cards += 1
            
            self.available_cards.remove(card)
            
            if self.player1_cards + self.player2_cards < 10:
                self.current_player = 2 if self.current_player == 1 else 1
                self.show_next_card()
            else:
                self.end_game()

    def end_game(self):
        p1_total = self.player1.get_total_rating()
        p2_total = self.player2.get_total_rating()
        
        if p1_total > p2_total:
            winner = "Player 1"
        elif p2_total > p1_total:
            winner = "Player 2"
        else:
            winner = "It's a tie"
        
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=f"Player 1 Total: {p1_total}"))
        content.add_widget(Label(text=f"Player 2 Total: {p2_total}"))
        content.add_widget(Label(text=f"Winner: {winner}"))
        
        popup = Popup(title="Game Over", content=content, size_hint=(0.8, 0.4))
        content.add_widget(Button(text="Close", on_press=popup.dismiss))
        popup.open()

class DraftApp(App):
    def build(self):
        Builder.load_file('draft.kv')
        return DraftGame()

if __name__ == '__main__':
    DraftApp().run()