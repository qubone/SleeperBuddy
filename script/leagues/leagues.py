from typing import List, Dict
from script.common.common import http_get_response_data
from enum import Enum

class RosterPosition(Enum):
    QB = 1
    RB = 2
    WR = 3
    TE = 4
    FLEX = 5
    SUPER_FLEX = 6
    DEF = 7
    K = 8
    BN = 9

class ScoringSettings():
    def __init__(self, score_settings: Dict[str, float]) -> None:
        self.fum: float = score_settings['fum']
        self.fum_lost: float = score_settings['fum_lost']
        #Rushing
        self.rush_yd: float = score_settings['rush_yd']
        self.rush_td: float = score_settings['rush_td']
        self.rush_2pt: float = score_settings['rush_2pt']
        #Receiving
        self.rec: float = score_settings['rec']
        self.rec_yd: float = score_settings['rec_yd']
        self.rec_td: float = score_settings['rec_td']
        self.bonus_rec_te: float = score_settings['bonus_rec_te']
        self.rec_2pt: float = score_settings['rec_2pt']
        #Passing
        self.pass_yd: float = score_settings['pass_yd']
        self.pass_td: float = score_settings['pass_td']
        self.pass_2pt: float = score_settings['pass_2pt']
        #Defense
        self.sack: float = score_settings['sack']
        self.int: float = score_settings['int']
        self.ff: float = score_settings['ff']
        self.fum_rec: float = score_settings['fum_rec']
        self.fum_rec_td: float = score_settings['fum_rec_td']
        self.pass_int: float = score_settings['pass_int']
        self.pass_int_td: float = score_settings['pass_int_td']
        self.def_td: float = score_settings['def_td']
        self.safe: float = score_settings['safe']
        self.pts_allow_0: float = score_settings['pts_allow_0']
        self.pts_allow_1_6: float = score_settings['pts_allow_1_6']
        self.pts_allow_7_13: float = score_settings['pts_allow_7_13']
        self.pts_allow_14_20: float = score_settings['pts_allow_14_20']
        self.pts_allow_21_17: float = score_settings['pts_allow_21_27']
        self.pts_allow_28_34: float = score_settings['pts_allow_28_34']
        self.pts_allow_35p: float = score_settings['pts_allow_35p']
        #Kicking
        self.fgmiss: float = score_settings['fgmiss']
        self.fgm_0_19: float = score_settings['fgm_0_19']
        self.fgm_20_29: float = score_settings['fgm_20_29']
        self.fgm_30_39: float = score_settings['fgm_30_39']
        self.fgm_40_49: float = score_settings['fgm_40_49']
        self.fgm_50p: float = score_settings['fgm_50p']
        self.xpm: float = score_settings['xpm']
        self.xpmiss: float = score_settings['xpmiss']
        #Special teams
        self.st_td: float = score_settings['st_td']
        self.st_ff: float = score_settings['st_ff']
        self.st_fum_rec: float = score_settings['st_fum_rec']
        self.def_st_fum_rec: float = score_settings['def_st_fum_rec']
        self.def_st_ff: float = score_settings['def_st_ff']
        self.def_st_td: float = score_settings['def_st_td']
        self.blk_kick: float = score_settings['blk_kick']
        #Optional
        if 'rush_td_40p' in score_settings:
            self.rush_td_40p: float = score_settings['rush_td_40p']
        if 'rush_td_50p' in score_settings:
            self.rush_td_50p: float = score_settings['rush_td_50p']
        if 'rec_td_40p' in score_settings:
            self.rec_td_40p: float = score_settings['rec_td_40p']
        if 'rec_td_50p' in score_settings:
            self.rec_td_50p: float = score_settings['rec_td_50p']


class Settings():
    def __init__(self, settings: dict) -> None:
        pass
        
class Metadata():
    def __init__(self, metadata: dict) -> None:
        pass


class LeagueData:
    def __init__(self, data: dict) -> None:
        self.total_rosters: int = data['total_rosters']
        self.loser_bracket_id: int = data['loser_bracket_id']
        self.group_id: int = data['group_id']
        self.bracket_id: int = data['bracket_id']
        self.last_transaction_id = data['last_transaction_id']
        self.roster_positions = [] # TODO: Create player position ['QB', 'RB', 'WR', 'TE', 'FLEX', 'SUPER_FLEX', 'BN', 'DEF', 'K']
        self.previous_league_id = data['previous_league_id']
        self.league_id: str = data['league_id']
        self.draft_id: str = data['draft_id']
        self.last_read_id: str = data['last_read_id']
        self.last_pinned_message_id: str = data['last_pinned_message_id']
        self.last_message_time: int = data['last_message_time']
        self.last_message_text_map = data['last_message_text_map']
        self.last_message_attachment = data['last_message_attachment']
        self.last_author_is_bot: bool = data['last_author_is_bot']
        self.last_author_id: str = data['last_author_id']
        self.last_author_display_name: str = data['last_author_display_name']
        self.last_author_avatar = data['last_author_avatar']
        self.display_order: int = data['display_order']
        self.last_message_id: str = data['last_message_id']
        self.scoring_settings = ScoringSettings(data['scoring_settings'])
        self.sport: str = data['sport']
        self.season_type: str = data['season_type'] # Check this part
        self.season: str = data['season']
        self.shard: int = data['shard']
        self.company_id = data['company_id']
        self.avatar = data['avatar']
        self.settings = {} # create settings "settings":{"daily_waivers_last_ran":30,"reserve_allow_cov":0,"reserve_slots":0,"leg":18,"offseason_adds":0,"bench_lock":0,"trade_review_days":2,"league_average_match":0,"waiver_type":0,"max_keepers":1,"type":0,"pick_trading":1,"disable_trades":1,"daily_waivers":0,"taxi_years":0,"trade_deadline":11,"veto_show_votes":0,"reserve_allow_sus":0,"reserve_allow_out":0,"playoff_round_type":0,"waiver_day_of_week":2,"taxi_allow_vets":0,"reserve_allow_dnr":0,"veto_auto_poll":0,"commissioner_direct_invite":0,"reserve_allow_doubtful":0,"waiver_clear_days":2,"playoff_week_start":0,"daily_waivers_days":5461,"last_scored_leg":18,"taxi_slots":0,"playoff_type":0,"daily_waivers_hour":0,"num_teams":12,"veto_votes_needed":8,"playoff_teams":6,"playoff_seed_type":0,"start_week":1,"reserve_allow_na":0,"draft_rounds":3,"taxi_deadline":0,"waiver_bid_min":0,"capacity_override":0,"disable_adds":1,"waiver_budget":100,"last_report":16,"best_ball":1},
        self.metadata = {} # create metadata "metadata":{"latest_league_winner_roster_id":"1","keeper_deadline":"0","copy_from_league_id":"860539001768112128","auto_continue":"off"}
        self.status: str = data['status'] #'complete'
        self.name: str = data['name'] # Glenn Hysén - bara ben BB


class Leagues:
    '''
    This endpoint retrieves all leagues.
    '''
    def __init__(self, user_id: str, season: str, sport: str = 'nfl', ) -> None:
        self.user_leagues = http_get_response_data(f'https://api.sleeper.app/v1/user/{user_id}/leagues/{sport}/{season}')
        self.user_id = user_id
        self.sport = sport
        self.season = season

    def get_leagues(self) -> List[LeagueData]:
        leagues = []
        for league in self.user_leagues:
            league_data = LeagueData(league)
            leagues.append(league_data)
        return leagues


    

