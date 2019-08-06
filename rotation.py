from fixtures import *
FPL_URL = "https://fantasy.premierleague.com/api/"


def intersection(lst1: List, lst2: List) -> List:
    return list(set(lst1) & set(lst2))


def find_two_man_rotation(start: int, end: int, teams_not_in_rotation: List[str]) -> List[str]:
    """
    :param start: It's the first gameweek of the rotation
    :param end: It's the last gameweek of the rotation
    :param teams_not_in_rotation: A list of teams that should not be included in the possible rotations
    :return: A list of pairs of teams who don't have hard fixtures in the same gameweeks
    """
    teams_dict = get_teams_dict()

    all_fixtures_strength = get_every_team_fixtures_strength(start, end)

    hard_fixtures_per_team = []

    for team_fixtures in all_fixtures_strength:
        hard_fixtures = get_hard_fixtures(team_fixtures)
        hard_fixtures_per_team.append(hard_fixtures)

    possibilities = []

    for i in range(1, len(all_fixtures_strength) + 1):
        for j in range(i + 1, len(all_fixtures_strength) + 1):
            if teams_not_in_rotation.count(str(teams_dict[i]['short_name'])) == 0 and \
               teams_not_in_rotation.count(str(teams_dict[j]['short_name'])) == 0 and \
               len(intersection(hard_fixtures_per_team[i - 1], hard_fixtures_per_team[j - 1])) == 0:
                possibilities.append(str(teams_dict[i]['short_name']) + ' - ' + str(teams_dict[j]['short_name']))

    return possibilities

