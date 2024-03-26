import random

MAX_NUM_OF_LINES= 5
MAX_BET = 100
MIN_BET = 5
MAX_SLIP = 3

premier_league_teams_2024 = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton & Hove Albion",
    "Burnley",
    "Chelsea",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Liverpool",
    "Luton",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham forest",
    "Sheffield United",
    "Tottenham Hotspur",
    "West Ham United",
    "Wolverhampton Wanderers"
]

def team_and_odds(list_of_teams):
    """takes a list of teams and generates random odds for each

    Args:
        list_of_teams (list)
    """
    team_dict = {}
    for team in list_of_teams:
        odds = random.uniform(1.0, 3.0)
        odds = '{:.2f}'.format(odds)
        team_dict[team] = odds
    return team_dict

def fixture_selection(list_of_teams):
    '''
    takes in the list of teams as an argument and returns random fixtures'''
    if len(list_of_teams) % 2 == 0:
        no_of_fixtures = 0.5 * len(list_of_teams)
        while True:
            for i in range(len(no_of_fixtures)):
                team_1 = random.choice(list_of_teams)
                list_of_teams.remove(team_1)
                team_2 = random.choice(list_of_teams)
                list_of_teams.remove(team_2)
                print(f"Fixture {i + 1}:{team_1} vs {team_2}")
            if i == no_of_fixtures:
                break
            
while True:
    num_of_team_parlay = int(input("how many teams would you like to parlay on? "))
    for i in range(num_of_team_parlay):
        input(f"Team {i}: ")
    

    
def deposit():
    while True:
        amount = int(input('How much would you like to deposit? $'))
        if amount.isdigit():
            if amount > 0:
                break
            else: 
                print('Amount must be more than $0')
        else:
            print('Please enter a valid number.')
    return amount


def get_bet():
    while True:
        amount = int(input('What would you like to bet? $'))
        if amount.isdigit():
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount has to be between {MIN_BET} and {MAX_BET}")
        else:
            print('Please enter a valid number.')
    return amount

def get_number_of_lines():
    while True:
        lines = int(input('How many lines would you like to bet on? $'))
        if lines.isdigit():
            if 1 <= lines <= MAX_NUM_OF_LINES:
                break
            else: 
                print('Line(s) must be more than $0')
        else:
            print('Please enter a valid number.')
    return lines

def parlay():
    
def main():
    balance = deposit()
    bet = get_bet()
    lines = get_number_of_lines()
    total_bet 
    
