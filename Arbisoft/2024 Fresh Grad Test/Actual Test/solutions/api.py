import requests
from collections import defaultdict
import sys


def get_year_from_date(date: str) -> int:
    """
    returns year part from a date in mm/dd/yyyy format
    """
    return int(date.split("/")[-1])


# weightage of the won match depends upon the year in which it was played
def get_weightage(current_year: int, match_year: int) -> float:
    """
    returns weightage of match played at specific year
    """
    weightage = 10 - (current_year - match_year)
    if weightage > 0:
        return weightage
    else:
        return 0.5


def get_total_from_scorecard(scorecard: list) -> int:
    """
    gets total team score form provided scorecard
    """
    total = 0
    for score in scorecard:
        total += score["score"]
    return total


# winning team is the one who scored highest
def get_winning_team(match: dict) -> str:
    """
    gets winning team in the match
    returns None in case of draw
    """
    team1 = match["team1"]
    team2 = match["team2"]
    team1_score = get_total_from_scorecard(match["scoreCardTeam1"])
    team2_score = get_total_from_scorecard(match["scoreCardTeam2"])
    if team1_score > team2_score:
        winning_team = team1
    elif team1_score < team2_score:
        winning_team = team2
    else:  # In case of draw
        winning_team = None
    return winning_team


def get_win_probability(matches: list, current_year: int, teams: list) -> dict:
    """
    returns win probability of both teams given in the teams list
    return value is a dict with keys as team names and values as win probability
    """
    obtained_weighted_points = defaultdict(lambda: 0)
    total_weighted_points = 0
    for match in matches:
        team1 = match["team1"]
        team2 = match["team2"]
        # Both input teams should be in the match
        # Continue otherwise
        if team1 not in teams or team2 not in teams:
            continue
        winning_team = get_winning_team(match)
        if winning_team is not None:
            match_year = get_year_from_date(match["date"])
            match_weightage = get_weightage(current_year, match_year)
            obtained_weighted_points[winning_team] += match_weightage
            total_weighted_points += match_weightage
    # win probability from above calculations will be
    win_probability = {}
    for team, points in obtained_weighted_points.items():
        win_probability[team] = (points / total_weighted_points) * 100
    return win_probability


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        teams = file.readline().strip().split(",")
    API_URL = (
        "https://l0l6pp2i0k.execute-api.eu-north-1.amazonaws.com/default/icc_matches"
    )
    CURRENT_YEAR = 2024
    matches = requests.get(API_URL).json()
    win_probabilites = get_win_probability(matches, CURRENT_YEAR, teams)
    team1 = teams[0]
    team2 = teams[1]
    print(f"{win_probabilites[team1]:.2f}%,", end="")
    print(f"{win_probabilites[team2]:.2f}%")
