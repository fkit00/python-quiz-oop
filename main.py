class User:
    def __init__(self, user_id, username):
        ## this will be called everytime we create a new object
        ##params following self will be passed in every time so User(8) would set an attribute
        ## any new objects must contain these pieces of data 
        self.id=user_id
        self.username= username
        self.followers=0
        self.following=0
        ## this means it's default and it doesn't need to be passed in
    def follow(self, user):
        ## always needs a self param as the first param
        user.followers +=1
        self.following +=1



user_1= User("001", "bruce")
user_2= User("002", "nancy")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
