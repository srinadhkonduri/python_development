# creating a user id
class User:
    def __init__(self, user_id, user_name):
        self.userId = user_id
        self.userName = user_name
        self.followers += 1
        self.following += 1

    def __int__(self, followers, following):
        self.followers = followers
        self.following = following


new_User = User("123", "sriandh")
print(new_User.userId)
print(new_User.userName)
