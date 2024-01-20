import pytest

#from script.main import SleeperUser, SleeperAvatar
from script.user.user import SleeperUser
from script.avatars.avatar import SleeperAvatar
from script.leagues.leagues import Leagues, League
from script.main import main

class Setup:
    def __init__(self) -> None:
        
        self.test_name = 'Linusbo'
        self.avatar = '88700289dc890fc9064fb95f84b1c3eb'
        
#TODO: MonkeyPatch


def test_get_user():
    user = SleeperUser("Linusbo")
    assert user.get_username() == 'Linusbo'
    assert user.get_user_id() == '727977584134025216'
    assert user.get_is_bot() == False
    assert user.get_display_name() == 'Linusbo'

def test_get_avatar():
    avatar = SleeperAvatar("88700289dc890fc9064fb95f84b1c3eb")
    assert avatar.get_avatar_id() == "88700289dc890fc9064fb95f84b1c3eb"
    assert avatar.get_avatar_url() == "https://sleepercdn.com/avatars/88700289dc890fc9064fb95f84b1c3eb"
    assert avatar.get_avatar_thumb_url() == "https://sleepercdn.com/avatars/thumbs/88700289dc890fc9064fb95f84b1c3eb"

def test_get_leagues():
    # https://api.sleeper.app/v1/user/727977584134025216/leagues/nfl/2023
    user_id = '727977584134025216'
    season = '2023'
    leagues = Leagues(user_id, season)
    test = leagues.get_leagues()
    print("TEST")


def test_get_specific_league():
    league = League('1004113252818726912')
    rosters = league.get_rosters()
    players = rosters[0].get_players()
    settings = rosters[0].get_roster_settings().get_ppts()
    print("TEST")

def test_main():
    main()