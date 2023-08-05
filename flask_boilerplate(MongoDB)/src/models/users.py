class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
        )

