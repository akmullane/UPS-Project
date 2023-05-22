# # Create a dictionary to store packages
# it will generate the fake package

import random
import ALL


class Package:
    def __init__(
        self,
        name,
        weight,
        types,
        size,
        origin,
        destination,
        pickup_time,
        status,
        location,
        referenceNum,
        estimate="00:00am",
        mileage=0,
    ):
        self.referenceNum = referenceNum
        self.name = name
        self.weight = weight
        self.types = types
        self.size = size
        self.origin = origin
        self.destination = destination
        self.pickup_time = pickup_time
        self.status = status
        self.location = location

        # self.estimate = ALL.getEstimate(origin, destination)
        # self.mileage = ALL.getDistance(origin, destination)

    # ===========================================================
    def getName(self):
        return self.name


# import random
# from package import Package
# import ALL


# # give the value to the packageclass
# # the variable name will be the 1z shipping label
# # this 1z lebat is 'package1' I will change it later
# package1 = Package(
#     name="Gain Mullane",
#     weight=random.randint(1, 100) / 10,
#     types="document",
#     size="4x4x3",
#     origin=office_A,
#     destination=office_B,
#     pickup_time="7:00am",
#     status="pending",
#     location="address",
#     referenceNum="123456",
# )

# # display
# ALL.print_package(package1)
# ALL.print_html(package1)
