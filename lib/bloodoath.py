class BloodOath:

    all = []

    def __init__(self, initiation_date, follower, cult):
        self.initiation_date = initiation_date
        self.cult = cult
        self.follower = follower
        BloodOath.all.append(self)

    def __repr__(self):
        return f"<BloodOath date={self.initiation_date}, follower={self.follower.name}, cult={self.cult.name}>"

    @classmethod
    def first_oath(cls):
        sorted_oaths = sorted(cls.all, key=lambda oath: oath.initiation_date)
        return sorted_oaths[0].follower

    def get_follower(self):
        return self._follower
    
    def set_follower(self, new_follower):
        if new_follower.age >= self.cult.minimum_age:
            self._follower = new_follower
        else:
            raise Exception(f"Thank you for your interest in joining {self.cult.name}.  Unfotunately, you must be at least {self.cult.minimum_age} years old to take the Blood Oath.  Please join when you are old enough.")

    follower = property(get_follower, set_follower)