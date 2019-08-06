from team import *

FPL_URL = "https://fantasy.premierleague.com/api/"
teams_dict = get_teams_dict()


def get_every_team_fixtures(first_gameweek: int, last_gameweek: int) -> List[List]:
    """
    :param first_gameweek: the first gameweek in the list of fixtures
    :param last_gameweek: the last gameweek in the list of fixtures
    :return: A list of all fixtures from every team between the first gameweek and the last gameweek.
             If you want the list of the opponents a team is facing you should access the list with index (id - 1)

    Example of return: [['NEW', 'BUR', 'LIV', 'TOT', 'WAT', 'AVL', 'MUN', 'BOU', 'SHU', 'CRY'],
                       ['TOT', 'BOU', 'EVE', 'CRY', 'WHU', 'ARS', 'BUR', 'NOR', 'BHA', 'MCI'],
                       ...
                       ['MCI', 'BHA', 'WAT', 'NOR', 'AVL', 'MUN', 'BOU', 'CRY', 'EVE', 'SHU'],
                       ['LEI', 'MUN', 'BUR', 'EVE', 'CHE', 'CRY', 'WAT', 'MCI', 'SOU', 'NEW']]
    """

    r = requests.get(FPL_URL + 'fixtures/')
    json_response = r.json()

    teams_fixtures = []

    for i in range(20):
        teams_fixtures.append([])

    for fixture in json_response:
        if last_gameweek >= fixture['event'] >= first_gameweek:
            teams_fixtures[fixture['team_h'] - 1].append(teams_dict[fixture['team_a']]['short_name'])
            teams_fixtures[fixture['team_a'] - 1].append(teams_dict[fixture['team_h']]['short_name'])

    return teams_fixtures


def get_every_team_fixtures_strength(first_gameweek: int, last_gameweek: int) -> List[int]:
    """
    :param first_gameweek: The first gameweek in the list of fixtures
    :param last_gameweek: The last gameweek in the list of fixtures
    :return: A list containing the strength of each opponent in each of the fixtures between the first
             gameweek and the last gameweek selected from every team.
             If you want the list of the opponents a team is facing you should access the list with index (id - 1)
    Example of return: [[3, 3, 5, 4, 3, 2, 4, 3, 2, 3],
                        [4, 3, 3, 3, 3, 4, 3, 2, 2, 5],
                        ...
                        [5, 2, 3, 2, 2, 4, 3, 3, 3, 2],
                        [3, 4, 3, 3, 4, 3, 3, 5, 3, 3]]
    """

    r = requests.get(FPL_URL + 'fixtures/')
    json_response = r.json()

    teams_fixtures = []

    for i in range(20):
        teams_fixtures.append([])

    for fixture in json_response:
        if last_gameweek >= fixture['event'] >= first_gameweek:
            teams_fixtures[fixture['team_h'] - 1].append(fixture['team_h_difficulty'])
            teams_fixtures[fixture['team_a'] - 1].append(fixture['team_a_difficulty'])

    print(teams_fixtures)
    return teams_fixtures


def get_hard_fixtures(fixtures: List[int]) -> List:
    """
    :param fixtures: A list of the strength of the opponent in each fixture during a certain period
    :return: A list containing the index of every gameweek that the opponent has a strength of 4 or 5
    """

    ret = []
    for i in range(len(fixtures)):
        if fixtures[i] > 3:
            ret.append(i)

    return ret
