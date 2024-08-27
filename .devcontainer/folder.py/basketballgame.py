class Player:
    def __init__(self, name, position, rating):
        self.name = name
        self.position = position
        self.rating = rating


class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        if len(self.players) < 5:
            self.players.append(player)


import random

positions = ["PG", "SG", "SF", "PF", "C"]
draft_pool = []

for i in range(50):  # Generate 50 players
    name = f"Player{i+1}"
    position = random.choice(positions)
    rating = random.randint(60, 99)
    draft_pool.append(Player(name, position, rating))


def draft_players(draft_pool):
    team1 = Team("Team 1")
    team2 = Team("Team 2")
    teams = [team1, team2]

    for i in range(5):  # Each team drafts 5 players
        for team in teams:
            print(f"{team.name}, it's your turn to draft.")
            for idx, player in enumerate(draft_pool):
                print(
                    f"{idx}: {player.name} ({player.position}) - Rating: {player.rating}"
                )
            choice = int(input("Choose a player by number: "))
            team.add_player(draft_pool.pop(choice))

    return team1, team2


def simulate_game(team1, team2):
    score1 = sum(player.rating for player in team1.players)
    score2 = sum(player.rating for player in team2.players)

    if score1 > score2:
        winner = team1.name
    elif score2 > score1:
        winner = team2.name
    else:
        winner = "Draw"

    return winner, score1, score2


def main():
    team1, team2 = draft_players(draft_pool)
    winner, score1, score2 = simulate_game(team1, team2)
    print(f"The winner is {winner} with scores {score1} - {score2}")


if __name__ == "__main__":
    main()
