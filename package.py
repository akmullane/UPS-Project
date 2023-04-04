# # Create a dictionary to store packages
#it will generate the fake package 

import random
import ALL

class Package:
    def __init__(self, name, weight, types, size, origin, destination, pickup_time, status, location,referenceNum,estimate = '00:00am',mileage = 0):
        self.name = name
        self.weight = weight
        self.types = types
        self.size = size
        self.origin = origin
        self.destination = destination
        self.pickup_time = pickup_time
        self.status = status
        self.location = location
        self.referenceNum = referenceNum
        self.estimate = ALL.getEstimate(origin,destination)
        self.mileage = ALL.getDistance(origin,destination)

    #===========================================================