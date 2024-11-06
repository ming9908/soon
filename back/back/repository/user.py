class UserTable:
    __tablename__ = "user"
    username = ""
    nick = ""

    def makeuser(self, username, nick):
        self.nick = nick
        self.username = username
