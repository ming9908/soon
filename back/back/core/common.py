from pydantic import BaseModel  # import BaseModel
from sqids import Sqids


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


# personal code
def make_user_code():
    sqids = Sqids()
    return sqids.encode([1, 2, 3])


def decode_user_code(id):
    sqids = Sqids()
    numbers = sqids.decode(id)
