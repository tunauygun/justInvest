class User:
    def __init__(self, username, roles):
        self._username = username
        self._roles = roles

    def get_username(self):
        return self._username

    def get_roles(self):
        return self._roles
