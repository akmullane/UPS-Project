import datetime
import requests


# Initialize application parameters
origin_pickup_points = ["Office A", "Office B"]
destination_pickup_points = ["Office B", "Office A"]
shuttle_frequency = "daily"
package_size = "document"
max_package_weight = 10  # in pounds
reusable_package_inventory = {"Package 1": {"weight_limit": 10, "mileage": 0},
                              "Package 2": {"weight_limit": 10, "mileage": 0}}

# Create a dictionary to store packages
packages = {}

# Define a function to schedule daily pickups
def schedule_pickup():
    pickup_time = datetime.datetime(2023, 3, 23, 15, 30)
    for origin in origin_pickup_points:
        package_weight = input(f"Enter the weight of the package from {origin}: ")
        if int(package_weight) > max_package_weight:
            print(f"Package from {origin} exceeds weight limit and cannot be picked up.")
        else:
            package_id = f"PKG{len(packages) + 1}"
            packages[package_id] = {"origin": origin, "destination": destination_pickup_points[origin_pickup_points.index(origin)],
                                    "weight": package_weight, "status": "In Transit", "ref_number": package_id}
            reusable_package = find_reusable_package(int(package_weight))
            if reusable_package:
                packages[package_id]["package"] = reusable_package
                reusable_package["mileage"] += calculate_mileage(origin, destination_pickup_points[origin_pickup_points.index(origin)])
            else:
                new_package = {"weight_limit": package_weight, "mileage": calculate_mileage(origin, destination_pickup_points[origin_pickup_points.index(origin)])}
                reusable_package_inventory[package_id] = new_package
                packages[package_id]["package"] = new_package
            print(f"Package {package_id} picked up from {origin} and will be delivered to {packages[package_id]['destination']} at {pickup_time}.")

# Define a function to find a reusable package that can hold the given weight
def find_reusable_package(package_weight):
    for package in reusable_package_inventory:
        if reusable_package_inventory[package]["weight_limit"] >= package_weight and reusable_package_inventory[package]["mileage"] < 500:
            return reusable_package_inventory[package]
    return None

# Define a function to calculate the distance between two pickup points
def calculate_mileage(origin, destination):
    # Implement your own method to calculate mileage
    return 50

# Define a function to track package status
def track_package(ref_number):
    if ref_number in packages:
        print(f"Package {ref_number} is currently {packages[ref_number]['status']} and is on its way to {packages[ref_number]['destination']}.")
    else:
        print(f"Package {ref_number} not found.")

# Define a function to update package status
def update_package_status(package_id, status):
    packages[package_id]["status"] = status

# Define a function to retire reusable packages
def retire_reusable_packages():
    for package in reusable_package_inventory:
        if reusable_package_inventory[package]["mileage"] >= 500:
            del reusable_package_inventory[package]

# Schedule daily pickups
schedule_pickup()

# Track package status
ref_number = input("Enter your package reference number: ")
track_package(ref_number)

# Update package status
package_id = input("Enter the package ID to update: ")
status = input("Enter the new status: ")
update_package_status(package_id, status)

# Retire reusable packages
retire_reusable_packages()

def generate_1z_label(ref_number):
    if ref_number in packages:
        # Call UPS API to generate label
        label = requests.post("https://www.ups.com/ship/v1/shipments",
                              headers={"Content-Type": "application/json", "AccessLicenseNumber": "YOUR_ACCESS_LICENSE_NUMBER", "Username": "YOUR_USERNAME", "Password": "YOUR_PASSWORD"},
                              json={"ShipmentRequest": {"Shipment": {"Shipper": {"Name": "John Doe", "ShipperNumber": "YOUR_SHIPPER_NUMBER", "Address": {"AddressLine": "123 Main St", "City": "Anytown", "StateProvinceCode": "NY", "PostalCode": "12345", "CountryCode": "US"}},"ShipTo": {"Name": "Jane Smith", "Address": {"AddressLine": "456 Broadway", "City": "New York", "StateProvinceCode": "NY", "PostalCode": "10012", "CountryCode": "US"}}, "ShipFrom": {"Name": "John Doe", "Address": {"AddressLine": "123 Main St", "City": "Anytown", "StateProvinceCode": "NY", "PostalCode": "12345", "CountryCode": "US"}}, "Service": {"Code": "03", "Description": "Service Code Description"}, "Package": {"PackagingType": {"Code": "02", "Description": "Customer Supplied Package"}, "PackageWeight": {"UnitOfMeasurement": {"Code": "LBS"}, "Weight": packages[ref_number]["weight"]}, "ReferenceNumber": {"Value": packages[ref_number]["ref_number"]}}}}}).json()

        # Return the label as a string
        return label["ShipmentResponse"]["ShipmentResults"]["PackageResults"]["ShippingLabel"]["GraphicImage"]
    else:
        return "Package not found."
#=========================================
#HTML FILE
#
# html_output = '''
# <!DOCTYPE html>
# <html>
# <head>
# 	<title>Additional Comments</title>
# </head>
# <body>
# '''
# html_output += "<h3>Additional Comments:</h3>"
# html_output += f"<p>To/From locations: {to_from_locations}</p>"
# html_output += f"<p>Package weight: {package_weight}</p>"
# html_output += f"<p>Tracking number: {tracking_number}</p>"
# html_output += f"<p>Shuttle time: {shuttle_time}</p>"
# html_output += f"<p>Mileage: {mileage}</p>"
# html_output += f"<p>Rating system: {rating_system}</p>"
# html_output += '''</body>
# </html>'''
#
# # Write the HTML code to a file
# with open("output.html", "w") as file:
#     file.write(html_output)
#
