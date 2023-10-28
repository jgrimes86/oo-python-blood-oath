import ipdb
from lib import *

# test your code here
# e.g.

f1 = Follower( 'Emiley', 31, 'Living the Dream' )
f2 = Follower( 'Steve', 26, "It's turtiles all the way down" )
f3 = Follower( 'Andrew', 48, "Any day now")
f4 = Follower( "F4", 30, "meaningful life motto")
f5 = Follower( "F5", 30, "meaningful life motto")
f6 = Follower( "F6", 30, "meaningful life motto")
f7 = Follower( "F7", 30, "meaningful life motto")
f8 = Follower( "F8", 30, "meaningful life motto")
f9 = Follower( "F9", 30, "meaningful life motto")
f10 = Follower( "F10", 30, "meaningful life motto")
f11 = Follower( "F11", 30, "meaningful life motto")
f12 = Follower( "F12", 30, "meaningful life motto")

f13 = Follower( "F13", 15, "life motto")
f14 = Follower( "F14", 80, "life motto")

c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )
c2 = Cult( "Church of Cookie Monster", "Los Angeles", 1968, "Did someone say cookies?", 18)
c3 = Cult( "LA Lakers", "Los Angeles", 1947, "I'm loving it.")
c4 = Cult( "Another Cult", "Las Vegas", 1974, "Don't be a dick.")
c5 = Cult( "Cult 5", "Los Angeles", 2022, "slogan 5")
c6 = Cult( "Cult 6", "San Diego", 1953, "slogan 6")

bo1 = BloodOath( '2019-09-16', f1, c1 )

bo2 = BloodOath( '2022-05-24', f2, c2 )

bo3 = BloodOath( '1996-03-14', f3, c2 )
bo4 = BloodOath( '1987-06-14', f3, c3 )

bo5 = BloodOath( '2023-10-28', f4, c1 )
bo6 = BloodOath( '2023-10-28', f4, c2 )

bo7 = BloodOath( '2023-10-28', f5, c1 )
bo8 = BloodOath( '2023-10-28', f5, c3 )

# bo9 = BloodOath( '2023-10-28', f6, c1 )
bo10 = BloodOath( '2023-10-28', f6, c4 )

bo11 = BloodOath( '2023-10-28', f7, c2 )
bo12 = BloodOath( '2023-10-28', f7, c3 )

bo13 = BloodOath( '2023-10-28', f8, c1 )
bo14 = BloodOath( '2023-10-28', f8, c2 )

bo15 = BloodOath( '2023-10-28', f9, c1 )
bo16 = BloodOath( '2023-10-28', f9, c2 )

bo17 = BloodOath( '2023-10-28', f10, c2 )
bo18 = BloodOath( '2023-10-28', f10, c3 )

bo19 = BloodOath( '2023-10-28', f11, c4 )
bo20 = BloodOath( '2023-10-28', f11, c2 )
bo21 = BloodOath( '2023-10-28', f11, c3 )

bo22 = BloodOath( '2023-10-28', f12, c1 )
bo23 = BloodOath( '2023-10-28', f12, c2 )
bo24 = BloodOath( '2023-10-28', f12, c3 )
bo25 = BloodOath( '2023-10-28', f12, c4 )


# c1.followers => ???
# f1.cults => ???




print( "Mwahahaha!" )
ipdb.set_trace()