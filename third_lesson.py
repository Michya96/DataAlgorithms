class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    def __repr__(self):
        return f"User(username='{self.username}', name='{self.name}', email='{self.email}')"
    def __str__(self):
        return self.__repr__()
    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}, I'm {self.name}! Contact me at {self.email}")


user1 = User('user1', 'Michael', 'Michja144@gmail.com')
user2 = User('user2', 'John', 'Johndoe@gmail.com')
print(user1)
user1.introduce_yourself('Pawel')