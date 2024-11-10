import random


def fetch_nba_players():
    return [
        {"name": "LeBron James", "position": "Forward", "rating": 99, "height": 78},
        {"name": "Stephen Curry", "position": "Guard", "rating": 96, "height": 75},
        {"name": "Kevin Durant", "position": "Forward", "rating": 97, "height": 81},
        {
            "name": "Giannis Antetokounmpo",
            "position": "Forward",
            "rating": 96,
            "height": 83,
        },
        {"name": "Nikola Jokic", "position": "Center", "rating": 96, "height": 82},
        {"name": "Joel Embiid", "position": "Center", "rating": 95, "height": 84},
        {"name": "Luka Doncic", "position": "Guard", "rating": 95, "height": 78},
        {"name": "Jayson Tatum", "position": "Forward", "rating": 94, "height": 80},
        {"name": "Ja Morant", "position": "Guard", "rating": 93, "height": 75},
        {"name": "Damian Lillard", "position": "Guard", "rating": 92, "height": 76},
        {"name": "Jimmy Butler", "position": "Guard", "rating": 91, "height": 79},
        {"name": "Anthony Davis", "position": "Center", "rating": 90, "height": 82},
        {"name": "Paul George", "position": "Forward", "rating": 90, "height": 81},
        {"name": "Kawhi Leonard", "position": "Forward", "rating": 90, "height": 79},
        {"name": "Devin Booker", "position": "Guard", "rating": 89, "height": 77},
        {"name": "Trae Young", "position": "Guard", "rating": 89, "height": 74},
        {"name": "Donovan Mitchell", "position": "Guard", "rating": 88, "height": 76},
        {
            "name": "Karl-Anthony Towns",
            "position": "Center",
            "rating": 88,
            "height": 83,
        },
        {"name": "Zach LaVine", "position": "Guard", "rating": 88, "height": 78},
        {"name": "Bradley Beal", "position": "Guard", "rating": 87, "height": 77},
        {"name": "Kyrie Irving", "position": "Guard", "rating": 87, "height": 75},
        {"name": "Bam Adebayo", "position": "Center", "rating": 87, "height": 81},
        {"name": "De'Aaron Fox", "position": "Guard", "rating": 86, "height": 76},
        {"name": "Pascal Siakam", "position": "Forward", "rating": 86, "height": 81},
        {"name": "Jaylen Brown", "position": "Guard", "rating": 86, "height": 79},
        {
            "name": "Shai Gilgeous-Alexander",
            "position": "Guard",
            "rating": 89,
            "height": 78,
        },
        {"name": "DeMar DeRozan", "position": "Guard", "rating": 85, "height": 79},
        {"name": "James Harden", "position": "Guard", "rating": 85, "height": 77},
        {"name": "Anthony Edwards", "position": "Guard", "rating": 84, "height": 78},
        {
            "name": "Kristaps Porzingis",
            "position": "Center",
            "rating": 84,
            "height": 85,
        },
        {"name": "Domantas Sabonis", "position": "Forward", "rating": 84, "height": 82},
        {"name": "Jrue Holiday", "position": "Guard", "rating": 84, "height": 77},
        {"name": "LaMelo Ball", "position": "Guard", "rating": 83, "height": 78},
        {"name": "Brandon Ingram", "position": "Forward", "rating": 83, "height": 80},
        {"name": "Zion Williamson", "position": "Forward", "rating": 83, "height": 79},
        {"name": "Fred VanVleet", "position": "Guard", "rating": 82, "height": 73},
        {"name": "CJ McCollum", "position": "Guard", "rating": 82, "height": 76},
        {"name": "Khris Middleton", "position": "Forward", "rating": 82, "height": 80},
        {"name": "Tyrese Haliburton", "position": "Guard", "rating": 81, "height": 77},
        {"name": "Jaren Jackson Jr.", "position": "Center", "rating": 81, "height": 82},
        {"name": "Scottie Barnes", "position": "Forward", "rating": 81, "height": 80},
        {"name": "Evan Mobley", "position": "Center", "rating": 81, "height": 83},
        {"name": "Paolo Banchero", "position": "Forward", "rating": 80, "height": 81},
        {"name": "Deandre Ayton", "position": "Center", "rating": 80, "height": 83},
        {"name": "Mikal Bridges", "position": "Forward", "rating": 80, "height": 79},
        {"name": "Desmond Bane", "position": "Guard", "rating": 80, "height": 77},
        {"name": "Cade Cunningham", "position": "Guard", "rating": 82, "height": 78},
        {"name": "Anfernee Simons", "position": "Guard", "rating": 79, "height": 76},
        {"name": "OG Anunoby", "position": "Forward", "rating": 79, "height": 79},
        {"name": "Walker Kessler", "position": "Center", "rating": 79, "height": 84},
        {"name": "Alperen Sengun", "position": "Center", "rating": 79, "height": 82},
        {"name": "Lauri Markkanen", "position": "Forward", "rating": 86, "height": 82},
        {"name": "Jalen Green", "position": "Guard", "rating": 78, "height": 77},
        {"name": "Tyrese Maxey", "position": "Guard", "rating": 85, "height": 75},
        {"name": "Bennedict Mathurin", "position": "Guard", "rating": 78, "height": 78},
        {
            "name": "Robert Williams III",
            "position": "Center",
            "rating": 78,
            "height": 81,
        },
        {"name": "Tobias Harris", "position": "Forward", "rating": 77, "height": 81},
        {"name": "Malcolm Brogdon", "position": "Guard", "rating": 77, "height": 77},
        {"name": "De'Andre Hunter", "position": "Forward", "rating": 77, "height": 79},
        {"name": "John Collins", "position": "Forward", "rating": 77, "height": 81},
        {"name": "Clint Capela", "position": "Center", "rating": 77, "height": 83},
        {"name": "Jarrett Allen", "position": "Center", "rating": 76, "height": 83},
        {"name": "Russell Westbrook", "position": "Guard", "rating": 76, "height": 76},
        {"name": "Andrew Wiggins", "position": "Forward", "rating": 76, "height": 80},
        {"name": "Marcus Smart", "position": "Guard", "rating": 76, "height": 76},
        {"name": "Myles Turner", "position": "Center", "rating": 76, "height": 83},
        {"name": "Jordan Poole", "position": "Guard", "rating": 75, "height": 77},
        {"name": "Keldon Johnson", "position": "Forward", "rating": 75, "height": 78},
        {"name": "Brook Lopez", "position": "Center", "rating": 75, "height": 84},
        {"name": "Kevin Love", "position": "Forward", "rating": 75, "height": 81},
        {"name": "Derrick White", "position": "Guard", "rating": 88, "height": 77},
        {"name": "Bogdan Bogdanovic", "position": "Guard", "rating": 74, "height": 78},
        {"name": "Gary Trent Jr.", "position": "Guard", "rating": 74, "height": 77},
        {"name": "Josh Giddey", "position": "Guard", "rating": 74, "height": 79},
        {"name": "Jusuf Nurkic", "position": "Center", "rating": 74, "height": 84},
        {"name": "Ivica Zubac", "position": "Center", "rating": 73, "height": 84},
        {"name": "Terry Rozier", "position": "Guard", "rating": 73, "height": 75},
        {"name": "Kyle Kuzma", "position": "Forward", "rating": 73, "height": 81},
        {"name": "Dillon Brooks", "position": "Guard", "rating": 73, "height": 77},
        {"name": "Harrison Barnes", "position": "Forward", "rating": 73, "height": 80},
        {"name": "Buddy Hield", "position": "Guard", "rating": 72, "height": 77},
        {"name": "Trey Murphy III", "position": "Forward", "rating": 72, "height": 80},
        {"name": "Jalen Brunson", "position": "Guard", "rating": 86, "height": 75},
        {"name": "Spencer Dinwiddie", "position": "Guard", "rating": 72, "height": 78},
        {"name": "Franz Wagner", "position": "Forward", "rating": 81, "height": 81},
        {"name": "Austin Reaves", "position": "Guard", "rating": 72, "height": 78},
        {"name": "Kelly Oubre Jr.", "position": "Forward", "rating": 71, "height": 79},
        {"name": "Norman Powell", "position": "Guard", "rating": 71, "height": 77},
        {"name": "Bojan Bogdanovic", "position": "Forward", "rating": 71, "height": 80},
        {"name": "Jakob Poeltl", "position": "Center", "rating": 71, "height": 84},
        {"name": "Immanuel Quickley", "position": "Guard", "rating": 71, "height": 76},
        {"name": "Markelle Fultz", "position": "Guard", "rating": 70, "height": 76},
        {
            "name": "Kentavious Caldwell-Pope",
            "position": "Guard",
            "rating": 70,
            "height": 78,
        },
        {"name": "Cameron Johnson", "position": "Forward", "rating": 70, "height": 81},
        {"name": "Nicolas Claxton", "position": "Center", "rating": 70, "height": 83},
        {"name": "Onyeka Okongwu", "position": "Center", "rating": 70, "height": 81},
        {"name": "Jalen Williams", "position": "Guard", "rating": 69, "height": 78},
        {"name": "Keegan Murray", "position": "Forward", "rating": 69, "height": 80},
        {"name": "Jeremy Sochan", "position": "Forward", "rating": 69, "height": 80},
        {
            "name": "Talen Horton-Tucker",
            "position": "Guard",
            "rating": 68,
            "height": 78,
        },
        {"name": "Trey Lyles", "position": "Forward", "rating": 68, "height": 82},
        {"name": "Monte Morris", "position": "Guard", "rating": 68, "height": 75},
        {"name": "Cole Anthony", "position": "Guard", "rating": 68, "height": 76},
        {"name": "Bones Hyland", "position": "Guard", "rating": 68, "height": 76},
        {"name": "Saddiq Bey", "position": "Forward", "rating": 68, "height": 79},
        {"name": "Michael Jordan", "position": "Guard", "rating": 99, "height": 78},
        {
            "name": "Kareem Abdul-Jabbar",
            "position": "Center",
            "rating": 98,
            "height": 86,
        },
        {"name": "Bill Russell", "position": "Center", "rating": 97, "height": 82},
        {"name": "Wilt Chamberlain", "position": "Center", "rating": 97, "height": 85},
        {"name": "Magic Johnson", "position": "Guard", "rating": 97, "height": 82},
        {"name": "Larry Bird", "position": "Forward", "rating": 96, "height": 80},
        {"name": "Tim Duncan", "position": "Forward", "rating": 95, "height": 84},
        {"name": "Shaquille O'Neal", "position": "Center", "rating": 95, "height": 85},
        {"name": "Hakeem Olajuwon", "position": "Center", "rating": 94, "height": 84},
        {"name": "Kobe Bryant", "position": "Guard", "rating": 94, "height": 79},
        {"name": "Oscar Robertson", "position": "Guard", "rating": 93, "height": 77},
        {"name": "Jerry West", "position": "Guard", "rating": 93, "height": 78},
        {"name": "Julius Erving", "position": "Forward", "rating": 92, "height": 79},
        {"name": "Moses Malone", "position": "Center", "rating": 92, "height": 83},
        {"name": "Karl Malone", "position": "Forward", "rating": 92, "height": 81},
        {"name": "John Stockton", "position": "Guard", "rating": 91, "height": 74},
        {"name": "David Robinson", "position": "Center", "rating": 91, "height": 85},
        {"name": "Charles Barkley", "position": "Forward", "rating": 90, "height": 79},
        {"name": "Scottie Pippen", "position": "Forward", "rating": 90, "height": 80},
        {"name": "Gary Payton", "position": "Guard", "rating": 89, "height": 77},
        {"name": "Jason Kidd", "position": "Guard", "rating": 89, "height": 78},
        {"name": "Steve Nash", "position": "Guard", "rating": 89, "height": 75},
        {"name": "Dirk Nowitzki", "position": "Forward", "rating": 88, "height": 84},
        {"name": "Dwyane Wade", "position": "Guard", "rating": 88, "height": 76},
        {"name": "Kevin Garnett", "position": "Forward", "rating": 88, "height": 83},
        {"name": "Allen Iverson", "position": "Guard", "rating": 87, "height": 74},
        {"name": "Patrick Ewing", "position": "Center", "rating": 87, "height": 84},
        {"name": "Clyde Drexler", "position": "Guard", "rating": 87, "height": 79},
        {"name": "Elgin Baylor", "position": "Forward", "rating": 86, "height": 78},
        {"name": "George Gervin", "position": "Guard", "rating": 86, "height": 79},
        {"name": "Isiah Thomas", "position": "Guard", "rating": 86, "height": 73},
        {"name": "Bob Cousy", "position": "Guard", "rating": 85, "height": 75},
        {"name": "Rick Barry", "position": "Forward", "rating": 85, "height": 79},
        {"name": "John Havlicek", "position": "Forward", "rating": 85, "height": 79},
        {
            "name": "Dominique Wilkins",
            "position": "Forward",
            "rating": 84,
            "height": 81,
        },
        {"name": "James Worthy", "position": "Forward", "rating": 84, "height": 82},
        {"name": "Bob Pettit", "position": "Forward", "rating": 83, "height": 80},
        {"name": "Walt Frazier", "position": "Guard", "rating": 83, "height": 78},
        {"name": "Dave Cowens", "position": "Center", "rating": 83, "height": 81},
        {"name": "Willis Reed", "position": "Center", "rating": 82, "height": 81},
        {"name": "Wes Unseld", "position": "Center", "rating": 82, "height": 80},
        {"name": "Dennis Rodman", "position": "Forward", "rating": 82, "height": 79},
        {"name": "Adrian Dantley", "position": "Forward", "rating": 81, "height": 77},
        {"name": "Alex English", "position": "Forward", "rating": 81, "height": 81},
        {"name": "Reggie Miller", "position": "Guard", "rating": 81, "height": 79},
        {"name": "Pete Maravich", "position": "Guard", "rating": 80, "height": 79},
        {"name": "Earl Monroe", "position": "Guard", "rating": 80, "height": 75},
        {"name": "Joe Dumars", "position": "Guard", "rating": 80, "height": 76},
        # ... (rest of the players)
    ]


def generate_draft_pool(num_players):
    players = fetch_nba_players()
    centers = random.sample([p for p in players if p["position"] == "Center"], 4)
    forwards = random.sample([p for p in players if p["position"] == "Forward"], 6)
    guards = random.sample([p for p in players if p["position"] == "Guard"], 6)
    remaining_players = [
        p for p in players if p not in centers and p not in forwards and p not in guards
    ]
    draft_pool = (
        centers + forwards + guards + random.sample(remaining_players, num_players - 16)
    )
    random.shuffle(draft_pool)
    return draft_pool


# prompt: write a python script to ensure each draft lottery has at least 2 forwards, 2 guards, and 1 center
# prompt: write a script which causes a new draft if there are not at least 2 centers, 3 forwards and 3 guards for in each half of the draft pool
def check_draft_pool(draft_pool):
    """
    Checks if there are at least 2 centers, 3 forwards and 3 guards for in each half of the draft pool.
    """
    half_point = len(draft_pool) // 2
    first_half = draft_pool[:half_point]
    second_half = draft_pool[half_point:]

    for half in [first_half, second_half]:
        centers = 0
        forwards = 0
        guards = 0
        for player in half:
            if player["position"] == "Center":
                centers += 1
            elif player["position"] == "Forward":
                forwards += 1
            elif player["position"] == "Guard":
                guards += 1
        if centers < 2 or forwards < 3 or guards < 3:
            return False

    return True


def draft_teams(draft_pool):
    team1 = {"Guard": [], "Forward": [], "Center": []}
    team2 = {"Guard": [], "Forward": [], "Center": []}

    pool1 = random.sample(draft_pool, 10)
    pool2 = [player for player in draft_pool if player not in pool1]

    for turn in range(5):
        for team_num, (team, pool) in enumerate(
            [(team1, pool1), (team2, pool2)], start=1
        ):
            print(f"\nTeam {team_num}, available players:")
            # Filter available players based on team needs
            available_players = []
            if len(team["Guard"]) < 3:
                available_players.extend([p for p in pool if p["position"] == "Guard"])
            if len(team["Forward"]) < 3:
                available_players.extend(
                    [p for p in pool if p["position"] == "Forward"]
                )
            if len(team["Center"]) < 2:
                available_players.extend([p for p in pool if p["position"] == "Center"])

            # Display available players
            for i, player in enumerate(available_players):
                print(
                    f"{i+1}. {player['name']} ({player['position']}, Skill Rating: {player['rating']}, Height Rating: {player['height']})"
                )

            valid_choice = False
            while not valid_choice:
                try:
                    choice = (
                        int(input("Enter the number of the player you want to draft: "))
                        - 1
                    )
                    chosen_player = available_players[choice]
                    team[chosen_player["position"]].append(
                        pool.pop(pool.index(chosen_player))
                    )
                    valid_choice = True
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid number from the list.")

    return team1, team2


def print_team(team, team_name):  # Added team_name argument
    print(f"\n{team_name}:")  # Print "Team 1" or "Team 2"
    for player in team["Guard"]:
        print(f"{player['name']} ({player['position']}, Rating: {player['rating']})")
    for player in team["Forward"]:
        print(f"{player['name']} ({player['position']}, Rating: {player['rating']})")
    for player in team["Center"]:
        print(f"{player['name']} ({player['position']}, Rating: {player['rating']})")


def simulate_game(team1, team2):
    # team1 and team2 are dictionaries of lists.  Each list needs to be iterated over to get the individual players.
    team1_rating = sum(
        player["rating"] for position in team1.values() for player in position
    ) + sum(player["height"] for position in team1.values() for player in position)
    team2_rating = sum(
        player["rating"] for position in team2.values() for player in position
    ) + sum(player["height"] for position in team2.values() for player in position)

    if team1_rating > team2_rating:
        return "Team 1"
    elif team2_rating > team1_rating:
        return "Team 2"
    else:
        return "It's a tie!"


if __name__ == "__main__":
    draft_pool = generate_draft_pool(20)
    team1, team2 = draft_teams(draft_pool)

    print_team(team1, "Team 1")
    print_team(team2, "Team 2")

    winner = simulate_game(team1, team2)
    print(f"\nThe winner is: {winner}")
