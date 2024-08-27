import random
from nba_api.stats.static import players

# Get the player dictionary
player_dict = players.get_players()

# Randomly select 5 players
random_players = random.sample(player_dict, 5)

# Print their names
for player in random_players:
    print(player["full_name"])
