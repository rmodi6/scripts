# We have decided to charge our passengers on the "great circle distance" traveled, and therefore will utilize the "spherical law of cosines" to calculate the distance around the Earth's circumference:
# 
# Let ($,x1) and (02, K2) be the latitude and longitude in radians of the two points 1 and 2.
# 
# Then the absolute difference in longitude is: A = K1 - K2 Then the angle between them is determined using the spherical law of cosines: = arccos(sin 1 sin 2+ cos 1 cos 2 cos(A))
# 
# Then the distance can be determined using d = radius Ao
# 
# You will be provided input that contains lines in two formats:
# 
# • LOC:CHI: 41836944 :-87.684722 where Loc describes the line format, CHI Is the name of the city whose location is being provided, 41836944 is the latitude of the city (in degrees) and - 87684722 is the longitude of the city (in degrees)
# 
# • TRIP:COFFEE10:CHI:NYC Where TRIP describes the line format, COFFEE is the account number of the passenger. CHI Is the city of departure, and NYC is the city of arrival.

import fileinput
from math import acos, sin, cos, radians, floor
RADIUS_MILES = 3963

class DestinationCalculator:
    def __init__(self):
        self.hmap = {}
    
    def process(self, line: str) -> str:
        split = line.split(':')
        if split[0] == 'LOC':
            self.hmap[split[1]] = (radians(float(split[2])), radians(float(split[3])))
            return split[1]
        else:
            fmat, account, source, destination = split
            phi1, k1 = self.hmap[source]
            phi2, k2 = self.hmap[destination]
            abs_long = abs(k1 - k2)
            angle = acos(sin(phi1)*sin(phi2) + cos(phi1)*cos(phi2)*cos(abs_long))
            distance = floor(RADIUS_MILES * angle)
            split.append(str(distance))
            return ':'.join(split[1:])
        
if __name__ == "__main__":
    dest_calc = DestinationCalculator()
    for line in fileinput.input():
        cleaned_line = line.replace("\n", "")
        print(dest_calc.process(cleaned_line))