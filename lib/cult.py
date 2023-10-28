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

    def average_age(self):
        total_ages = 0
        for follower in self.cult_members():
            total_ages += follower.age
        return float(total_ages / self.cult_population())
    
    def followers_mottos(self):
        for follower in self.cult_members():
            print(follower.life_motto)

    @classmethod
    def least_popular(cls):
        return sorted(cls.all, key=lambda cult: cult.cult_population())[0]

    @classmethod
    def most_common_location(cls):
        cult_locations_list = [cult.location for cult in cls.all]
        commonest_location = ""
        count_number = 0
        for location in cult_locations_list:
            if cult_locations_list.count(location) > count_number:
                commonest_location = location
                count_number = cult_locations_list.count(location)
        return commonest_location



