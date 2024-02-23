''' All data related to players. '''
from typing import Dict, List, Any

class PlayerPersonal:
    ''' Class for personal player data. '''
    def __init__(self,  player_db: Dict[str, Any]) -> None:
        self.full_name = player_db['full_name']
        self.age = player_db['age']
        self.weight = player_db['weight']
        self.height = player_db['height']
        self.birth_date = player_db['birth_date']
        self.college = player_db['college']
        self.high_school = player_db['high_school']

    def get_full_name(self) -> str:
        ''' Returns the full name of the player. '''
        return self.full_name

    def get_first_name(self) -> str:
        ''' Returns the last name of the player. '''
        return str(self.full_name.split(" "))[0]

    def get_last_name(self) -> str:
        ''' Returns the first name of the player. '''
        return str(self.full_name.split(" "))[1]

    def get_age(self) -> int:
        ''' Returns the age of the player. '''
        return self.age

    def get_weight(self) -> str:
        ''' Returns the weight (lbs) of the player. '''
        return self.weight

    def get_height(self) -> str:
        ''' Returns the height (ft) of the player. '''
        return self.height

    def get_birth_date(self) -> str:
        ''' Returns the last of the player. '''
        return self.birth_date

    def get_college(self) -> str:
        ''' Returns the last college of the player. '''
        return self.college

    def get_high_scool(self) -> str:
        ''' Returns the high school of the player. '''
        return self.high_school


class PlayerProfessional:
    ''' Class for professional player data. '''
    def __init__(self,  player_db: Dict[str, Any]) -> None:
        self.years_exp = player_db['years_exp']
        self.team = player_db['team']
        self.number = player_db['number']
        self.position = player_db['position']
        self.status = player_db['status']
        self.depth_chart_order = player_db['depth_chart_order']

    def get_years_exp(self) -> int:
        ''' Returns the number of years experience of the player. '''
        return self.years_exp

    def get_team(self) -> int:
        ''' Returns the current team of the player. '''
        return self.team

    def get_number(self) -> int:
        ''' Returns the current number of the player. '''
        return self.number

    def get_position(self) -> int:
        ''' Returns the position of the player. '''
        return self.position

    def get_status(self) -> str:
        ''' Returns the status of the player. '''
        return self.status

    def get_depth_chart_order(self) -> int:
        ''' Returns the current depth chart of the player. '''
        return self.depth_chart_order


class PlayerSleeper:
    ''' Handling of Sleeper-related player data. '''
    def __init__(self,  player_db: Dict[str, Any]) -> None:
        self.player_id = player_db['player_id']
        self.metadata = player_db['metadata']
        self.fantasy_data_id = player_db['fantasy_data_id']
        self.fantasy_positions = player_db['fantasy_positions']

    def get_player_id(self) -> str:
        ''' Returns the Sleeper ID of the player. '''
        return self.player_id

    def get_metadata(self) -> Dict[str, str]:
        ''' Returns the Sleeper metadata of the player. '''
        return self.metadata

    def get_fantasy_data_id(self) -> int:
        ''' Returns the Sleeper fantasy data ID of the player. '''
        return self.fantasy_data_id

    def get_fantasy_positions(self) -> List[str]:
        ''' Returns the Sleeper fantasy positions of the player. '''
        return self.fantasy_positions


class Player:
    ''' Constructs player data based on the player ID. '''
    def __init__(self, player_db: Dict[str, Any]) -> None:
        self.player_db = player_db
        self.personal = PlayerPersonal(self.player_db)
        self.professional = PlayerProfessional(self.player_db)
        self.sleeper_data = PlayerSleeper(self.player_db)

    def get_personal_data(self) -> PlayerPersonal:
        ''' Returns all personal data. '''
        return self.personal

    def get_professional_data(self) -> PlayerProfessional:
        ''' Returns all professional data. '''
        return self.professional

    def get_sleeper_data(self) -> PlayerSleeper:
        ''' Returns all sleeper data. '''
        return self.sleeper_data
