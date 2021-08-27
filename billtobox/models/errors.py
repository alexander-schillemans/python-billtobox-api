from .base import BaseModel

class Error(BaseModel):

    def __init__(self,
        path=None,
        error=None,
        message=None,
        status=None
    ):

        self.path = path
        self.error = error
        self.message = message
        self.status = status