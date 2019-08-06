import requests
from typing import Dict, List

FPL_URL = "https://fantasy.premierleague.com/api/"


def get_teams_info() -> List:
    """
    :return: A list containing the details of all teams
    """
    r = requests.get(FPL_URL + 'bootstrap-static/')
    json_response = r.json()
    teams = json_response['teams']

    for team in teams:
        team.pop('draw', None)
        team.pop('loss', None)
        team.pop('played', None)
        team.pop('points', None)
        team.pop('position', None)
        team.pop('form', None)
        team.pop('team_division', None)
        team.pop('unavailable', None)
        team.pop('win', None)
        team.pop('strength_defence_home', None)
        team.pop('strength_defence_away', None)
        team.pop('strength_attack_home', None)
        team.pop('strength_attack_away', None)
    return teams


def get_teams_dict() -> Dict:
    """
    :return: A dictionary where the key is the id of the team and the value is the team itself
    """
    teams = get_teams_info()
    teams_dict = {}

    for team in teams:
        teams_dict[team['id']] = team

    return teams_dict
