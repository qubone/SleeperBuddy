from pathlib import Path
from typing import List
import pytest

from script.common.common import write_json_to_file, read_json_from_file
from script.user.user import SleeperUser
from script.avatars.avatar import SleeperAvatar
from script.leagues.leagues import (Leagues, League, LeagueRoster, 
                                    RosterMetadata, RosterSettings,
                                    RosterWaiverData, RosterScoring)


class Setup:
    ''' Setup class for shared test input data. '''
    def __init__(self) -> None:
        self.user_name = 'Linusbo'
        self.user_id = '727977584134025216'
        self.league_id = '1004113252818726912'
        self.season = '2023'
        self.avatar = '88700289dc890fc9064fb95f84b1c3eb'       
        self.test_roster_path = Path(
            'test/resources/test_single_roster.json'
            )
        self.test_roster_settings_path = Path(
            'test/resources/test_roster_settings.json'
            )
        self.players_path = Path('test/resources/test_player_data.json')
        self.user_path = Path('test/resources/test_sleeper_user.json')
        self.roster_data = read_json_from_file(
            self.test_roster_path
            )
        self.roster_settings_data = read_json_from_file(
            self.test_roster_settings_path
            )
        self.players = read_json_from_file(
            self.players_path
            )
        self.user_data = read_json_from_file(
            self.user_path
            )
        self.league = League('1004113252818726912')
        self.roster = LeagueRoster(self.roster_data)
        self.roster_settings = RosterSettings(self.roster_settings_data)
        self.user = SleeperUser(self.user_data)
        #self.settings = self.roster.get_roster_settings()

        self.test_url = 'https://api.sleeper.app/v1/user/727977584134025216/leagues/nfl/2023'
        self.database = "script/resources/players_db.json"
        
        #TODO: MonkeyPatch


@pytest.fixture(name="setup")
def setup_fixture():
    ''' Pytest decorator to use shared Setup class for testing. '''
    return Setup()


def test_get_user(setup: Setup):
    ''' Test Sleeper User data. '''
    assert isinstance(setup.user, SleeperUser)
    assert setup.user.get_username() == 'linusbo'
    assert setup.user.get_user_id() == '727977584134025216'
    assert setup.user.get_is_bot() is False
    assert setup.user.get_display_name() == 'Linusbo'


def test_get_avatar(setup: Setup):
    ''' Test Sleeper User avatar. '''
    avatar = SleeperAvatar(setup.avatar)
    assert avatar.get_avatar_id() == "88700289dc890fc9064fb95f84b1c3eb"
    assert avatar.get_avatar_url() == \
        "https://sleepercdn.com/avatars/88700289dc890fc9064fb95f84b1c3eb"
    assert avatar.get_avatar_thumb_url() ==  \
        "https://sleepercdn.com/avatars/thumbs/88700289dc890fc9064fb95f84b1c3eb"


def test_get_leagues(setup: Setup):
    ''' Test for retrieving all leagues a user have joined per season. '''
    leagues = Leagues(setup.user_id, setup.season)
    all_user_leagues = leagues.get_leagues()
    assert len(all_user_leagues) == 13


def test_get_league_rosters(setup: Setup):
    ''' Test number of rosters retrieved. '''
    rosters = setup.league.get_rosters()
    assert isinstance(rosters, list)
    assert len(rosters) == 8


def test_get_roster(setup: Setup):
    ''' Test for fetching league roster data. '''
    assert isinstance(setup.roster, LeagueRoster)
    assert isinstance(setup.roster.get_roster_settings(), RosterSettings)
    assert isinstance(setup.roster.get_roster_metadata(), RosterMetadata)
    assert isinstance(setup.roster.get_roster_players(setup.database), list)
    assert len(setup.roster.get_player_ids()) == 22
    assert len(setup.roster.get_roster_players(setup.database)) == 22
    assert len(setup.roster.get_starter_players(setup.database)) == 12


def test_get_roster_settings(setup: Setup):
    ''' Test for fetching the roster settings. '''
    settings = setup.roster.get_roster_settings()
    assert isinstance(settings, RosterSettings)
    assert isinstance(settings.get_waiver_data(), RosterWaiverData)
    assert isinstance(settings.get_scoring_data(), RosterScoring)
    assert settings.get_wins() == 9
    assert settings.get_losses() == 5
    assert settings.get_ties() == 0


def test_get_roster_waiver_data(setup: Setup):
    ''' Test for fetching the roster waiver data. . '''
    waiver_data = setup.roster_settings.get_waiver_data()
    assert isinstance(waiver_data, RosterWaiverData)
    assert waiver_data.get_waiver_position() == 8
    assert waiver_data.get_waiver_budget_used() == 0
    assert waiver_data.get_total_moves() == 0


def test_get_roster_scoring_data(setup: Setup):
    ''' Test for fetching the roster waiver data. . '''
    scoring_data = setup.roster_settings.get_scoring_data()
    assert isinstance(scoring_data, RosterScoring)
    assert scoring_data.get_fantasy_points_scored() == 2982.2
    assert scoring_data.get_fantasy_points_allowed() == 2888.78

def test_get_specific_league(setup: Setup):
    league = League('1004113252818726912')
    league.league_url
    league.league_rosters
    rosters = league.get_rosters()
    output = Path('test_rosters.json')
    write_json_to_file(league.league_rosters, output.resolve())

    output2 = Path('test_league.json')
    write_json_to_file(league.league_url, output2.resolve())
    players = rosters[0].get_roster_players(setup.database)
    settings = rosters[0].get_roster_settings().get_ppts()
    print("TEST")

#def test_roster_metadata():

def test_get_all_players():
    test_get_all_players()

def test_main():
    main()