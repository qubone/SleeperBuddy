''' Parser for Sleeper API. '''
from typing import Dict, Any, Union
import requests


class SleeperAPIParser:
    ''' Parses data from Sleeper API with HTTP GET using requests library. '''
    def __init__(self) -> None:
        self.base_url = 'https://api.sleeper.app/v1/'

    def _http_get_response_data_json(
            self, url: str
            ) -> Union[Dict[str, Any] | None]:
        ''' Returns HTTP GET in JSON format. '''
        response = requests.get(url, timeout=None)
        return response.json() if response.status_code == 200 else None

    def get_players(self):
        ''' Parses all player data. '''
        return self._http_get_response_data_json(
            f'{self.base_url}/players/nfl'
            )

    def get_user(self, user: str):
        ''' Parses user data. '''
        return self._http_get_response_data_json(
            f'{self.base_url}/user/{user}'
            )

    def get_league(self, league_id: str):
        ''' Parses league data. '''
        return self._http_get_response_data_json(
            f'{self.base_url}/league/{league_id}'
            )

    def get_league_rosters(self, league_id: str):
        ''' Parses league rosters. '''
        return self._http_get_response_data_json(
            f'{self.base_url}/league/{league_id}/rosters'
            )
