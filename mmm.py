#! /usr/bin/env python
# coding: utf-8
# Author:  Shai Rubinstein
# Date:    October 2022
# Summary:
#! /usr/bin/env python
# coding: utf-8
# Author:  Shai Rubinstein
# Date:    October 2022
# Summary:
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

#connect to api
sc = OAuth2(None, None, from_file='fantasy_app.json')

if __name__ == "__main__":
    gm = yfa.Game(sc, 'nba')
    print(gm)
    league_ids = gm.league_ids()
    print(league_ids)
    league = gm.to_league('395.l.152079')
    print(league.standings())
    print(league)
    all_teams_keys = league.teams()
    keys = all_teams_keys.keys()
    team_keys = all_teams_keys['402.l.180453.t.1'].keys()
    # team = league.to_team(team_key)
    # print(team)
    # roster = team.roster()
    # print(roster)
