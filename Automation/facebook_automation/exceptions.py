

class UrlException(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg
        super().__init__(self.msg)
    
    def __str__(self) -> str:
        return self.msg

class NotChosenException(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg
        super().__init__(self.msg)
    
    def __str__(self) -> str:
        return self.msg


class NotChosenException(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg
        super().__init__(self.msg)
    
    def __str__(self) -> str:
        return self.msg

    
