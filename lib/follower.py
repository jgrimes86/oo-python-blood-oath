from .bloodoath import BloodOath
import datetime

class Follower:

    all = []

    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        Follower.all.append(self)

    def __repr__(self):
        return f"<Follower name={self.name}>"
    
    def cults(self):
        return [oath.cult for oath in BloodOath.all if oath.follower == self]

    def join_cult(self, cult):
        initiation_date = datetime.date.today()
        BloodOath(initiation_date, self, cult)

    @classmethod
    def of_a_certain_age(cls, searched_age):
        return [follower for follower in cls.all if follower.age >= searched_age]

    def my_cults_slogans(self):
        for cult in self.cults():
            print(cult.slogan)
    
    @classmethod
    def most_active(cls):
        bloodoath_followers = [oath.follower for oath in BloodOath.all]
        most_active_follower = []
        initiation_count = 0
        for follower in bloodoath_followers:
            if bloodoath_followers.count(follower) > initiation_count:
                most_active_follower = follower
                initiation_count = bloodoath_followers.count(follower)
        return most_active_follower

    @classmethod
    def top_ten(cls):
        bloodoath_followers = [oath.follower for oath in BloodOath.all]
        followers_set = set(bloodoath_followers)
        follower_activity_list = []
        for follower in followers_set:
            follower_dict = {follower: bloodoath_followers.count(follower)}
            follower_activity_list.append(follower_dict)

        def sort_function(follower_dict):
            values = list(follower_dict.values())
            return values[0]

        sorted_followers = sorted(follower_activity_list, key=sort_function, reverse=True)

        return sorted_followers[0:10]
    
    def fellow_cult_members(self):
        fellow_followers = []
        for cult in self.cults():
            for member in cult.cult_members():
                if member not in fellow_followers:
                    fellow_followers.append(member)
        return fellow_followers
