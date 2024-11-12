from pydantic import BaseModel  # import BaseModel


class response:
    success: bool
    message: str
    data: any

    def __init__(self):
        self.success = False

    @classmethod
    def set_success(self):
        self.success = True
        self.message = ""

    def set_data(self, data: any):
        self.data = data
