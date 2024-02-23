''' Handling of Sleeper user data. '''
from typing import Dict, Any
from script.avatars.avatar import SleeperAvatar


class SleeperUser:
    '''
    Via the user resource, you can GET the user object
    by either providing the username or user_id of the user. '''
    def __init__(self, user_data: Dict[str, Any]) -> None:
        self.user_data = user_data
        self.user_name = self.user_data["username"]
        self.user_id = self.user_data["user_id"]
        self.is_bot = self.user_data["is_bot"]
        self.display_name = self.user_data["display_name"]
        self.avatar = SleeperAvatar(self.user_data["avatar"])

    def get_username(self) -> str:
        ''' Returns the Sleeper user name. '''
        return self.user_name

    def get_user_id(self) -> str:
        ''' Returns the Sleeper user ID. '''
        return self.user_id

    def get_is_bot(self) -> bool:
        ''' Returns if User is bot. '''
        return self.is_bot

    def get_display_name(self) -> str:
        ''' Returns Sleeper display name. '''
        return self.display_name

    def get_avatar(self) -> SleeperAvatar:
        ''' Returns Sleeper avatar. '''
        return self.avatar
