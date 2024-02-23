''' Handling of Sleeper Avatar data '''


class SleeperAvatar:
    '''
    Users and leagues have avatar images. 
    There are thumbnail and full-size images for each avatar.
    '''
    def __init__(self, avatar_id: str) -> None:
        self.avatar_id = avatar_id
        self.avatar_url = f'https://sleepercdn.com/avatars/{avatar_id}'
        self.avatar_thumb_url = f'https://sleepercdn.com/avatars/thumbs/{avatar_id}'

    def get_avatar_id(self) -> str:
        ''' Returns the avatar id. '''
        return self.avatar_id

    def get_avatar_url(self) -> str:
        ''' Returns the avatar id url. '''
        return self.avatar_url

    def get_avatar_thumb_url(self) -> str:
        ''' Returns the avatar thumbnail url. '''
        return self.avatar_thumb_url
