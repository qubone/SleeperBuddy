from typing import List, Dict
from script.common.common import http_get_response_data
from script.players.players import Player
from enum import Enum
from decimal import Decimal


TRUE = 1
FALSE = 0

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

class LeagueType(Enum):
    REDRAFT = 0
    KEEPER  = 1
    DYNASTY = 2

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
        if 'pass_int_td' in score_settings:
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

class LeagueSettings():
    def __init__(self, settings: dict) -> None:
        self.daily_waivers_last_ran: int = settings['daily_waivers_last_ran']
        self.reserve_allow_cov: int = settings['reserve_allow_cov']
        self.reserve_slots: int = settings['reserve_slots']
        self.leg: int = settings['leg']
        self.offseason_adds: int = settings['offseason_adds']
        self.bench_lock: int = settings['bench_lock']
        self.trade_review_days: int = settings['trade_review_days']
        self.league_average_match: int = settings['league_average_match']
        self.waiver_type: int = settings['waiver_type'] # 0 Rolling Waivers 1 Reverse Standings 2 FAAB bidding
        self.max_keepers: int = settings['max_keepers']
        self.type:LeagueType = settings['type']
        self.pick_trading: int = settings['pick_trading']
        self.disable_trades: int = settings['disable_trades']
        self.daily_waivers: int = settings['daily_waivers']
        self.taxi_years: int = settings['taxi_years']
        self.trade_deadline: int = settings['trade_deadline']
        if 'veto_show_votes' in settings:
            self.veto_show_votes: int = settings['veto_show_votes']
        self.reserve_allow_sus: int = settings['reserve_allow_sus']
        self.playoff_round_type: int = settings['playoff_round_type']
        self.waiver_day_of_week: int = settings['waiver_day_of_week']
        self.waiver_day_of_week: int = settings['waiver_day_of_week']
        self.taxi_allow_vets: int = settings['taxi_allow_vets']
        self.reserve_allow_dnr: int = settings['reserve_allow_dnr']
        if 'veto_auto_poll' in settings:
            self.veto_auto_poll: int = settings['veto_auto_poll']
        self.commissioner_direct_invite: int = settings['commissioner_direct_invite']
        self.reserve_allow_doubtful: int = settings['reserve_allow_doubtful']
        self.waiver_clear_days: int = settings['waiver_clear_days']
        self.playoff_week_start: int = settings['playoff_week_start']
        self.daily_waivers_days: int = settings['daily_waivers_days']
        self.last_scored_leg: int = settings['last_scored_leg']
        self.taxi_slots: int = settings['taxi_slots']
        self.playoff_type: int = settings['playoff_type']
        self.daily_waivers_hour: int = settings['daily_waivers_hour']
        self.num_teams: int = settings['num_teams']
        if 'veto_votes_needed' in settings:
            self.veto_votes_needed: int = settings['veto_votes_needed']
        self.playoff_teams: int = settings['playoff_teams']
        self.playoff_seed_type: int = settings['playoff_seed_type'] #Playoff Seeding rules 0 Default 1 Re-seed
        self.start_week: int = settings['start_week']
        self.reserve_allow_na: int = settings['reserve_allow_na']
        self.draft_rounds: int = settings['draft_rounds']
        self.taxi_deadline: int = settings['taxi_deadline']
        if 'waiver_bid_min' in settings:
            self.waiver_bid_min: int = settings['waiver_bid_min']
        self.capacity_override: int = settings['capacity_override']
        self.disable_adds: int = settings['disable_adds']
        self.waiver_budget: int = settings['waiver_budget']
        self.last_report: int = settings['last_report']
        self.best_ball: int = settings['best_ball'] #1 True 0 False

    # Leage type
    def is_best_ball(self) -> bool:
        return True if self.best_ball == TRUE else False
    def is_redraft(self) -> bool:
        return True if self.type == LeagueType.REDRAFT else False
    def is_keeper(self) -> bool:
        return True if self.type == LeagueType.KEEPER else False
    def is_dynasty(self) -> bool:
        return True if self.type == LeagueType.DYNASTY else False
    
    #Playoffs
    def get_number_of_playoff_teams(self) -> int:
        return self.playoff_teams
    
    #Taxi
    def get_number_of_taxi_slots(self) -> int:
        return self.taxi_slots
    def get_number_of_taxi_years(self) -> int:
        return self.taxi_years



class Metadata():
    def __init__(self, meta_data: dict) -> None:
        if 'latest_league_winner_roster_id' in meta_data:
            self.latest_league_winner_roster_id: str = meta_data['latest_league_winner_roster_id']
        self.keeper_deadline: str = meta_data['keeper_deadline']
        if 'copy_from_league_id' in meta_data:
            self.copy_from_league_id: str = meta_data['copy_from_league_id']
        self.auto_continue: str = meta_data['auto_continue']

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
        self.league_settings = LeagueSettings(data['settings'])
        self.metadata = Metadata(data['metadata'])
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
    
class RosterMetadata():
    def __init__(self, metadata: Dict[str, str]) -> None:
        self.streak: str = metadata['streak']
        self.record: str = metadata['record']
    def get_winning_streak(self) -> str:
        return self.streak
    def get_game_record(self) -> str:
        return self.record
    def get_number_of_wins(self) -> int:
        # for each W in number of games list
        pass
    def get_number_of_losses(self) -> int:
        #number of games - wins
        pass

class RosterSettings():
    def __init__(self, settings_data: Dict[str, int]) -> None:
        self.wins = settings_data['wins']
        self.waiver_position = settings_data['waiver_position']
        self.waiver_budget_used = settings_data['waiver_budget_used']
        self.total_moves = settings_data['total_moves']
        self.ties = settings_data['ties']
        self.ppts_decimal: int = settings_data['ppts_decimal']
        self.ppts: int = settings_data['ppts']
        self.losses: int = settings_data['losses']
        self.fpts_decimal: int = settings_data['fpts_decimal']
        self.fpts_against_decimal: int = settings_data['fpts_against_decimal']
        self.fpts_against: int = settings_data['fpts_against']
        self.fpts: int = settings_data['fpts']
    def get_wins(self) -> int:
        return self.wins
    def get_losses(self) -> int:
        return self.losses
    def get_waiver_position(self) -> int:
        return self.waiver_position
    def get_waiver_budget_used(self) -> int:
        return self.waiver_budget_used
    def get_total_moves(self) -> int:
        return self.total_moves
    def get_ties(self) -> int:
        return self.ties
    def get_ppts(self) -> int:
        #TODO: Refactor this
        exact_ppts = Decimal(str(self.ppts)) + Decimal('.' + str(self.ppts_decimal))
        return float(exact_ppts.real)
    def get_fpts(self) -> int:
        #TODO: Refactor this
        exact_fpts = Decimal(str(self.fpts)) + Decimal('.' + str(self.fpts_decimal))
        return float(exact_fpts.real)
    def get_fpts_against(self) -> int:
        #TODO: Refactor this
        exact_pts_against = Decimal(str(self.pts_against)) + Decimal('.' + str(self.fpts_against_decimal))
        return float(exact_pts_against.real)


class LeagueRoster():
    def __init__(self, roster_data: dict) -> None:
        self.taxi = roster_data['taxi']
        self.starters = roster_data['starters']
        self.settings = RosterSettings(roster_data['settings'])
        self.roster_id: int = roster_data['roster_id']
        self.reserve = roster_data['reserve']
        self.players = roster_data['players']
        self.player_map = roster_data['player_map']
        self.owner_id: str = roster_data['owner_id']
        self.metadata = RosterMetadata(roster_data['metadata'])
        self.league_id: str = roster_data['league_id']
        self.keepers = roster_data['keepers']
        self.co_owners = roster_data['co_owners']
    
    def get_players(self) -> List[Player]:
        players = []
        for player in self.players:
            players.append(Player(player))
        return players
    
    def get_starters(self) -> List[Player]:
        starters = []
        for player in self.starters:
            starters.append(Player(player))
        return starters
    def get_roster_settings(self) -> RosterSettings:
        return self.settings

class League():
    '''
    This endpoint retrieves a specific league.
    '''
    def __init__(self, league_id: str) -> None:
        self.league_url = http_get_response_data(f'https://api.sleeper.app/v1/league/{league_id}')
        self.league_rosters = http_get_response_data(f'https://api.sleeper.app/v1/league/{league_id}/rosters')
        self.test = None

    def get_league(self) -> LeagueData:
        return LeagueData(self.league_url)
    
    def get_rosters(self) -> List[LeagueRoster]:
        rosters = []
        for roster in self.league_rosters:
            rosters.append(LeagueRoster(roster))
        return rosters


    




