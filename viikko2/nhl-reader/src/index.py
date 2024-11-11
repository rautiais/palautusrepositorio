import requests
import inquirer
from rich.console import Console
from rich.table import Table
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def user_input():
    nationalities = ["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS", "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"]
    sorted_nationalities = sorted(nationalities)

    seasons = {"2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"}
    sorted_seasons = sorted(seasons)

    questions = [inquirer.List('season', message="Select season", choices=sorted_seasons),
                inquirer.List('nationality', message="Select nationality", choices=sorted_nationalities)]
    
    answers = inquirer.prompt(questions)
    return answers['season'], answers['nationality']
    
def player_display(players):
    console = Console()
    table = Table(show_header=True)
    table.add_column("name")
    table.add_column("team")
    table.add_column("goals")
    table.add_column("assists")
    table.add_column("points")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.all_points()))
    
    console.print(table)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    season, nationality = user_input()
    players = stats.top_scorers_by_nationality(nationality)

    player_display(players)

if __name__ == "__main__":
    main()
