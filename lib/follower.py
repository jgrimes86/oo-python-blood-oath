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
    
