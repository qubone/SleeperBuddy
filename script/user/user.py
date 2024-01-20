from script.avatars.avatar import SleeperAvatar
from script.common.common import http_get_response_data
class SleeperUser:
    '''
    Via the user resource, you can GET the user object by either providing the username or user_id of the user.
    '''
    def __init__(self, user: str) -> None:
        self.response_data = http_get_response_data(f'https://api.sleeper.app/v1/user/{user}')
        self.user_name = user
        self.user_id = self.response_data["user_id"]
        self.is_bot = self.response_data["is_bot"]
        self.display_name = self.response_data["display_name"]
        self.avatar = SleeperAvatar(self.response_data["avatar"])
    def get_username(self) -> str:
        return self.user_name
    def get_user_id(self) -> str:
        return self.user_id
    def get_is_bot(self) -> bool:
        return self.is_bot
    def get_display_name(self) -> str:
        return self.display_name
    def get_avatar(self) -> SleeperAvatar:
        return self.avatar