import random
import time
import pandas as pd
import matplotlib.pyplot as plt


from players import fetch_nba_players


def generate_draft_pool(num_players):
    players = fetch_nba_players()
    positions = {"Center": 4, "Forward": 6, "Guard": 6}
    draft_pool = []

    for position, count in positions.items():
        draft_pool.extend(
            random.sample([p for p in players if p["position"] == position], count)
        )

    remaining_players = [p for p in players if p not in draft_pool]
    draft_pool.extend(random.sample(remaining_players, num_players - len(draft_pool)))
    random.shuffle(draft_pool)
    return draft_pool


def draft_teams(draft_pool):
    teams = [{"Guard": [], "Forward": [], "Center": []} for _ in range(2)]
    pools = [random.sample(draft_pool, 10), []]
    pools[1] = [player for player in draft_pool if player not in pools[0]]

    for turn in range(5):
        for team_num, (team, pool) in enumerate(zip(teams, pools), start=1):
            print(f"\nTeam {team_num}, available players:")
            available_players = [
                p
                for p in pool
                if len(team[p["position"]]) < (3 if p["position"] != "Center" else 2)
            ]

            for i, player in enumerate(available_players):
                print(
                    f"{i+1}. {player['name']} ({player['position']}, Skill: {player['rating']}, Height: {player['height']})"
                )

            while True:
                try:
                    choice = (
                        int(input("Enter the number of the player you want to draft: "))
                        - 1
                    )
                    chosen_player = available_players[choice]
                    team[chosen_player["position"]].append(
                        pool.pop(pool.index(chosen_player))
                    )
                    print(f"Great choice! You've drafted {chosen_player['name']}!")
                    break
                except (ValueError, IndexError):
                    print("Invalid input. Please enter a valid number from the list.")

    return teams


def auto_draft(draft_pool):
    teams = [{"Guard": [], "Forward": [], "Center": []} for _ in range(2)]
    pools = [random.sample(draft_pool, 10), []]
    pools[1] = [player for player in draft_pool if player not in pools[0]]

    for turn in range(5):
        for team_num, (team, pool) in enumerate(zip(teams, pools), start=1):
            available_players = [
                p
                for p in pool
                if len(team[p["position"]]) < (3 if p["position"] != "Center" else 2)
            ]
            if available_players:
                chosen_player = random.choice(available_players)
                team[chosen_player["position"]].append(
                    pool.pop(pool.index(chosen_player))
                )
    return teams


def print_team(team, team_name):
    print(f"\n{team_name}:")
    for position in team:
        for player in team[position]:
            print(
                f"{player['name']} ({player['position']}, Rating: {player['rating']}, Height: {player['height']})"
            )


def calculate_team_chemistry(team):
    chemistry = 0
    for position in team.values():
        for player in position:
            # Players with ratings above 90 boost team chemistry
            if player["rating"] > 90:
                chemistry += 5
            # Players with ratings between 85-90 slightly boost chemistry
            elif 85 <= player["rating"] <= 90:
                chemistry += 3
    return chemistry


def team_rating(team):
    return sum(
        player["rating"] + player["height"] / 2
        for position in team.values()
        for player in position
    )


def pre_game_visualization(team1, team2):
    team1_rating = team_rating(team1) + calculate_team_chemistry(team1)
    team2_rating = team_rating(team2) + calculate_team_chemistry(team2)

    if team1_rating > team2_rating:
        projected_winner = "Team 1"
    elif team2_rating > team1_rating:
        projected_winner = "Team 2"
    else:
        projected_winner = "Tie"

    team1_ratings = [
        player["rating"] for position in team1.values() for player in position
    ]
    team2_ratings = [
        player["rating"] for position in team2.values() for player in position
    ]

    plt.figure(figsize=(10, 6))

    # Team 1 bar
    bottom = 0
    for i, rating in enumerate(team1_ratings):
        plt.bar(
            "Team 1", rating, bottom=bottom, color=plt.cm.Blues(i / len(team1_ratings))
        )
        bottom += rating

    # Team 2 bar
    bottom = 0
    for i, rating in enumerate(team2_ratings):
        plt.bar(
            "Team 2", rating, bottom=bottom, color=plt.cm.Reds(i / len(team2_ratings))
        )
        bottom += rating

    plt.ylabel("Overall Rating")
    plt.title(f"Team Overall Ratings\nProjected Winner: {projected_winner}")

    # Create legend handles and labels
    handles = []
    labels = []
    for i, player in enumerate(team1.values()):
        for p in player:
            handles.append(
                plt.Rectangle((0, 0), 1, 1, color=plt.cm.Blues(i / len(team1_ratings)))
            )
            labels.append(p["name"])
    for i, player in enumerate(team2.values()):
        for p in player:
            handles.append(
                plt.Rectangle((0, 0), 1, 1, color=plt.cm.Reds(i / len(team2_ratings)))
            )
            labels.append(p["name"])

    plt.legend(
        handles, labels, loc="upper left", bbox_to_anchor=(1, 1), title="Players"
    )
    plt.show()


def print_team(team, team_name):
    print(f"\n{team_name}:")
    for position in team:
        for player in team[position]:
            print(
                f"{player['name']} ({player['position']}, Rating: {player['rating']})"
            )


def simulate_game(team1, team2):
    def team_rating(team):
        return sum(
            player["rating"] + player["height"] / 2
            for position in team.values()
            for player in position
        )

    team1_rating = team_rating(team1) + calculate_team_chemistry(team1)
    team2_rating = team_rating(team2) + calculate_team_chemistry(team2)

    print("\nSimulating the game...")
    time.sleep(2)

    quarters = [1, 2, 3, 4]
    team1_score = 0
    team2_score = 0

    # Initialize player stats dictionaries
    team1_stats = {}
    team2_stats = {}
    for position in team1:
        for player in team1[position]:
            team1_stats[player["name"]] = {"points": 0, "rebounds": 0, "assists": 0}
    for position in team2:
        for player in team2[position]:
            team2_stats[player["name"]] = {"points": 0, "rebounds": 0, "assists": 0}

    for quarter in quarters:
        print(f"\nQuarter {quarter}:")

        # Calculate quarter points based on player stats
        team1_quarter = 0
        for player in team1_stats:
            points = random.randint(0, 10) + int(
                next(
                    p["height"]
                    for pos in team1
                    for p in team1[pos]
                    if p["name"] == player
                )
                / 50
            )
            team1_stats[player]["points"] += points
            team1_quarter += points

        team2_quarter = 0
        for player in team2_stats:
            points = random.randint(0, 10) + int(
                next(
                    p["height"]
                    for pos in team2
                    for p in team2[pos]
                    if p["name"] == player
                )
                / 50
            )
            team2_stats[player]["points"] += points
            team2_quarter += points

        team1_score += team1_quarter
        team2_score += team2_quarter

        # Distribute points, rebounds, and assists based on height
        for player in team1_stats:
            height = next(
                p["height"] for pos in team1 for p in team1[pos] if p["name"] == player
            )
            rating = next(
                p["rating"] for pos in team1 for p in team1[pos] if p["name"] == player
            )
            position = next(
                p["position"]
                for pos in team1
                for p in team1[pos]
                if p["name"] == player
            )

            if position == "Guard":
                rebounds = random.choices(range(0, 3), weights=[1, 2, 3], k=1)[0] + (
                    int((height - 70) / 5)
                )
                assists = random.randint(1, 3) + int(rating / 40)
            elif position == "Forward":
                rebounds = random.choices(range(0, 3), weights=[1, 2, 3], k=1)[0] + (
                    int((height - 72) / 5)
                )
                assists = random.randint(1, 2) + int(rating / 45)
            elif position == "Center":
                rebounds = random.choices(range(0, 6), weights=[1, 2, 3, 4, 5, 6], k=1)[
                    0
                ] + (int((height - 72) / 5))
                assists = random.randint(1, 2) + int(rating / 47)

            team1_stats[player]["rebounds"] += rebounds
            team1_stats[player]["assists"] += assists

        for player in team2_stats:
            height = next(
                p["height"] for pos in team2 for p in team2[pos] if p["name"] == player
            )
            rating = next(
                p["rating"] for pos in team2 for p in team2[pos] if p["name"] == player
            )
            position = next(
                p["position"]
                for pos in team2
                for p in team2[pos]
                if p["name"] == player
            )

            if position == "Guard":
                rebounds = random.choices(range(0, 3), weights=[1, 2, 3], k=1)[0] + (
                    int((height - 70) / 5)
                )
                assists = random.randint(1, 3) + int(rating / 40)
            elif position == "Forward":
                rebounds = random.choices(range(0, 3), weights=[1, 2, 3], k=1)[0] + (
                    int((height - 72) / 5)
                )
                assists = random.randint(1, 2) + int(rating / 45)
            elif position == "Center":
                rebounds = random.choices(range(0, 6), weights=[1, 2, 3, 4, 5, 6], k=1)[
                    0
                ] + (int((height - 72) / 5))
                assists = random.randint(1, 2) + int(rating / 47)

            team2_stats[player]["rebounds"] += rebounds
            team2_stats[player]["assists"] += assists

        print(f"Team 1: {team1_quarter} points")
        print(f"Team 2: {team2_quarter} points")
        print(f"Current Score - Team 1: {team1_score}, Team 2: {team2_score}")
        time.sleep(2)

    print("\nFinal Score:")
    print(f"Team 1: {team1_score}")
    print(f"Team 2: {team2_score}")

    # Print individual player reports
    print("\nTeam 1 Player Reports:")
    for player, stats in team1_stats.items():
        print(
            f"{player}: Points - {stats['points']}, Rebounds - {stats['rebounds']}, Assists - {stats['assists']}"
        )
    print("\nTeam 2 Player Reports:")
    for player, stats in team2_stats.items():
        print(
            f"{player}: Points - {stats['points']}, Rebounds - {stats['rebounds']}, Assists - {stats['assists']}"
        )

    return "Team 1", team1_score, team2_score, team1_stats, team2_stats

    if team1_score > team2_score:
        return "Team 1", team1_score, team2_score
    elif team2_score > team1_score:
        return "Team 2", team1_score, team2_score
    else:
        return "It's a tie!", team1_score, team2_score


def play_game(team1, team2):
    winner, team1_score, team2_score, team1_stats, team2_stats = simulate_game(
        team1, team2
    )  # Modified this line to return team1_stats and team2_stats
    # Modified this line to return team1_stats and team2_stats
    # Assuming team1_stats and team2_stats are the dictionaries from simulate_game

    # Create DataFrames
    team1_df = pd.DataFrame(team1_stats).T
    team2_df = pd.DataFrame(team2_stats).T

    # --- Visualization 1: Points per player ---
    plt.figure(figsize=(12, 6))
    plt.bar(team1_df.index, team1_df["points"], label="Team 1", color="blue")
    plt.bar(team2_df.index, team2_df["points"], label="Team 2", color="red")
    plt.xlabel("Players", fontsize=12)
    plt.ylabel("Points", fontsize=12)
    plt.title("Points per Player", fontsize=14)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.legend(fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

    # --- Visualization 2: Rebounds & Assists per player ---
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()

    ax1.bar(
        team1_df.index,
        team1_df["rebounds"],
        label="Team 1 Rebounds",
        color="blue",
        alpha=0.7,
    )
    ax1.bar(
        team2_df.index,
        team2_df["rebounds"],
        label="Team 2 Rebounds",
        color="red",
        alpha=0.7,
    )
    ax2.plot(
        team1_df.index,
        team1_df["assists"],
        marker="o",
        label="Team 1 Assists",
        color="blue",
    )
    ax2.plot(
        team2_df.index,
        team2_df["assists"],
        marker="x",
        label="Team 2 Assists",
        color="red",
    )

    ax1.set_xlabel("Players", fontsize=12)
    ax1.set_ylabel("Rebounds", fontsize=12)
    ax2.set_ylabel("Assists", fontsize=12)
    plt.title("Rebounds & Assists per Player", fontsize=14)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    fig.legend(
        loc="upper left",
        bbox_to_anchor=(0, 1),
        bbox_transform=ax1.transAxes,
        fontsize=10,
    )
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

    # --- Visualization 3: Total stats per team ---
    team_totals = pd.DataFrame({"Team 1": team1_df.sum(), "Team 2": team2_df.sum()})
    team_totals.plot(kind="bar", figsize=(10, 6), color=["blue", "red"])
    plt.ylabel("Total", fontsize=12)
    plt.title("Total Points, Rebounds, and Assists per Team", fontsize=14)
    plt.xticks(rotation=0, fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

    # --- Visualization 4: Player Performance ---
    plt.figure(figsize=(12, 6))
    for player in team1_stats:
        plt.plot(team1_df.loc[player], marker="o", label=player)
    for player in team2_stats:
        plt.plot(team2_df.loc[player], marker="x", label=player)
    plt.xlabel("Stats", fontsize=12)
    plt.ylabel("Value", fontsize=12)
    plt.title("Player Performance", fontsize=14)
    plt.legend(fontsize=8, ncol=2)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()
    print(f"\nThe winner is: {winner}")
    return winner, team1_score, team2_score, team1_stats, team2_stats


if __name__ == "__main__":
    print("Welcome to the NBA Draft and Game Simulator!")
    draft_pool = generate_draft_pool(20)

    print("\nDrafting teams...")

    # Ask the user if they want to auto-draft
    auto_draft_choice = input("Do you want to auto-draft teams? (yes/no): ")
    if auto_draft_choice.lower() == "yes":
        team1, team2 = auto_draft(draft_pool)
    else:
        team1, team2 = draft_teams(draft_pool)

    print("\nFinal Team Rosters:")
    print_team(team1, "Team 1")
    print_team(team2, "Team 2")

    pre_game_visualization(
        team1, team2
    )  # Pregame visualization is called before the input prompt

    input(
        "\nPress Enter to start the game simulation..."
    )  # Input prompt to start the simulation

    winner, team1_score, team2_score, team1_stats, team2_stats = play_game(team1, team2)

    print("\nGame Statistics:")
    print(f"Team 1 Score: {team1_score}")
    print(f"Team 2 Score: {team2_score}")
    print(f"Margin of Victory: {abs(team1_score - team2_score)} points")
