

class Player():
    def __init__(self, player_id: str) -> None:
        self.name = None
        self.player_id: str = player_id
        self.age = None
        self.experience = None
        self.team = None

    def is_rookie(self) -> bool:
        if self.experience == 0:
            return True
    def get_player_id(self) -> str:
        return self.player_id

class Quarterback(Player):
    def __init__(self) -> None:
        pass
        
class RunnningBack(Player):
    def __init__(self) -> None:
        pass
        
class WideReceiver(Player):
    def __init__(self) -> None:
        pass

class TightEnd(Player):
    def __init__(self) -> None:
        pass

class Kicker(Player):
    def __init__(self) -> None:
        pass

class Defense():
    def __init__(self) -> None:
        pass
