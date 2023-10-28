class BloodOath:

    all = []

    def __init__(self, initiation_date, follower, cult):
        self.initiation_date = initiation_date
        self.follower = follower
        self.cult = cult
        BloodOath.all.append(self)

    def __repr__(self):
        return f"<BloodOath date={self.initiation_date}, follower={self.follower.name}, cult={self.cult.name}>"