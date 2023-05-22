

import random
from Address import office_A,office_B
from package import Package
import ALL



# give the value to the packageclass
#the variable name will be the 1z shipping label
#this 1z lebat is 'package1' I will change it later
package1 = Package(
    name= 'Gain Mullane',
    weight=random.randint(1, 100) / 10,
    types='document',
    size='4x4x3',
    origin=office_A,
    destination=office_B,
    pickup_time='7:00am',
    status='pending',
    location='address',
    referenceNum='123456'
)

#display
ALL.print_package(package1)
ALL.print_html(package1)



# package2 = Package(
#     name='Gain Mullane',
#     weight=random.randint(1, 100) / 10,
#     types='document',
#     size='4x4x3',
#     origin=office_A,
#     destination=office_B,
#     pickup_time='7:00am',
#     status='pending',
#     location='address',
#      referenceNum='0909090'
# )

# packageList= {'TrackingNumber1': package1 , 'TrackingNumber2': package2}
      
# reusable_package_inventory = {
#     "Package 1": {"weight_limit": 10, "mileage":0},
#     "Package 2": {"weight_limit": 10, "mileage": 0}}



# Define a function to schedule daily pickups

  

# # Define a function to find a reusable package that can hold the given weight
# def find_reusable_package(package_weight):
#     for package in reusable_package_inventory:
#         if reusable_package_inventory[package]["weight_limit"] >= package_weight and reusable_package_inventory[package]["mileage"] < 500:
#             return reusable_package_inventory[package]
#     return None

# # Define a function to calculate the distance between two pickup points
# def calculate_mileage(origin, destination):
#     # Implement your own method to calculate mileage
#     return 50

# # Define a function to track package status
# def track_package(ref_number):
#     if ref_number in packages:
#         print(f"Package {ref_number} is currently {packages[ref_number]['status']} and is on its way to {packages[ref_number]['destination']}.")
#     else:
#         print(f"Package {ref_number} not found.")

# # Define a function to update package status
# def update_package_status(package_id, status):
#     packages[package_id]["status"] = status

# # Define a function to retire reusable packages
# def retire_reusable_packages():
#     for package in reusable_package_inventory:
#         if reusable_package_inventory[package]["mileage"] >= 500:
#             del reusable_package_inventory[package]

# # Schedule daily pickups
# schedule_pickup()

# # Track package status
# ref_number = input("Enter your package reference number: ")
# track_package(ref_number)

# # Update package status
# package_id = input("Enter the package ID to update: ")
# status = input("Enter the new status: ")
# update_package_status(package_id, status)

# # Retire reusable packages
# retire_reusable_packages()
# '''

# '''
# #=========================================
# #HTML FILE
# #
# # html_output = '''
# # <!DOCTYPE html>
# # <html>
# # <head>
# # 	<title>Additional Comments</title>
# # </head>
# # <body>
# # '''
# # html_output += "<h3>Additional Comments:</h3>"
# # html_output += f"<p>To/From locations: {to_from_locations}</p>"
# # html_output += f"<p>Package weight: {package_weight}</p>"
# # html_output += f"<p>Tracking number: {tracking_number}</p>"
# # html_output += f"<p>Shuttle time: {shuttle_time}</p>"
# # html_output += f"<p>Mileage: {mileage}</p>"
# # html_output += f"<p>Rating system: {rating_system}</p>"
# # html_output += '''</body>
# # </html>'''
# #
# # # Write the HTML code to a file
# # with open("output.html", "w") as file:
# #     file.write(html_output)
# #

