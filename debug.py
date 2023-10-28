import ipdb
from lib import *

# test your code here
# e.g.

f1 = Follower( 'Emiley', 31, 'Living the Dream' )
f2 = Follower( 'Steve', 25, "It's turtiles all the way down" )
f3 = Follower( 'Andrew', 48, "Any day now")

c1 = Cult( 'Heavens Gate', 'San Diego', 1974, 'Human Metamorphosis' )
c2 = Cult( "Church of Cookie Monster", "Los Angeles", 1968, "Did someone say cookies?" )
c3 = Cult( "LA Lakers", "Los Angeles", 1947, "I'm loving it." )
c4 = Cult( "Another Cult", "Las Vegas", 1974, "Don't be a dick." )

bo1 = BloodOath( '2019-09-16', f1, c1 )
bo2 = BloodOath( '2022-05-24', f2, c1 )
bo3 = BloodOath( '1996-03-14', f3, c2 )
bo4 = BloodOath( '1987-06-14', f3, c3 )



# c1.followers => ???
# f1.cults => ???




print( "Mwahahaha!" )
ipdb.set_trace()