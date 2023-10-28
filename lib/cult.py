from .bloodoath import BloodOath
import datetime

class Cult:

    all = []

    def __init__(self, name, location, founding_year, slogan):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        Cult.all.append(self)

    def __repr__(self):
        return f"<Cult name={self.name}>"

    def recruit_follower(self, follower_instance):
        oath_date = datetime.date.today()
        BloodOath(oath_date, follower_instance, self)

    def cult_members(self):
        return [oath.follower for oath in BloodOath.all if oath.cult == self]

    def cult_population(self):
        return len(self.cult_members())

    @classmethod
    def find_by_name(cls, searched_name):
        found_cult = [cult for cult in cls.all if cult.name == searched_name]
        return found_cult[0]
    
    @classmethod
    def find_by_location(cls, searched_location):
        return [cult for cult in cls.all if cult.location == searched_location]

    @classmethod
    def find_by_founding_year(cls, searched_year):
        return [cult for cult in cls.all if cult.founding_year == searched_year]