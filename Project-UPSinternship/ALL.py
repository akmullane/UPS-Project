import os
import requests
import json
import mysql.connector
import math
import webbrowser
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('API_KEY')


last_update_time = None
last_result_set = None

# =====================================
def get_distance(origin, destination):
    # Call the Google Maps Distance Matrix API to get the travel time and distance
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={origin}&destinations={destination}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    distance = float(data["rows"][0]["elements"][0]["distance"]["text"].split(" ")[0])
    return distance
# =====================================
def get_estimate(origin, destination):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={origin}&destinations={destination}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    travel_time = float(
        data["rows"][0]["elements"][0]["duration"]["text"].split(" ")[0]
    )
    return travel_time
# =====================================
def find_nearby_store(origin):
    address = origin

    # Use the Geocoding API to get the latitude and longitude of the address
    geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    geocoding_response = requests.get(geocoding_url).json()
    latitude = geocoding_response["results"][0]["geometry"]["location"]["lat"]
    longitude = geocoding_response["results"][0]["geometry"]["location"]["lng"]

    # Use the Places API to search for UPS stores near the address
    places_url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&type=store&keyword=UPS&fields=name,vicinity,formatted_address&key={api_key}"
    places_response = requests.get(places_url).json()

    # Check if there are any results
    if "results" not in places_response:
        print("Error: No results found in API response.")
        print(json.dumps(places_response, indent=2))
        exit()

    # Extract the name and address of the nearest UPS store
    if len(places_response["results"]) > 0:
        nearest_store = places_response["results"][0]
        if "formatted_address" in nearest_store:
            store_address = nearest_store["formatted_address"]
        elif "vicinity" in nearest_store:
            store_address = nearest_store["vicinity"]
        else:
            store_address = "Unknown"
        store_name = nearest_store["name"]
    #     print(f"The nearest UPS store to {address} is {store_name} at {store_address}.")
    else:
        print("No UPS stores found within 5000 meters of the specified address.")
    return store_address
# =====================================
def open_map(origin, destination):
    # Create the URL for the Google Maps directions
    url = f"https://www.google.com/maps/dir/{origin}/{destination}"
    
    # Open the URL in a web browser
    webbrowser.open(url)
# =====================================
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.asin(math.sqrt(a))
    r = 3956  # Radius of earth in miles
    return c * r
# =====================================
def find_nearby_driver(origin, max_distance=10):
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="Gain044298809", database="tracking"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM driver")

    driver_addresses = []
    driver_ID = []
    driver_names = []

    myresult1 = mycursor.fetchall()
    for row in myresult1:
        driver_addresses.append(row[2])
        driver_ID.append(row[0])
        driver_names.append(row[1])

       
    # Use the Geocoding API to get the latitude and longitude of the address
    geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={origin}&key={api_key}"
    geocoding_response = requests.get(geocoding_url).json()
    origin_lat = geocoding_response["results"][0]["geometry"]["location"]["lat"]
    origin_lon = geocoding_response["results"][0]["geometry"]["location"]["lng"]

    # Calculate the straight-line distance between the origin and each driver's address
    distances = []
    for address in driver_addresses:
        geocoding_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
        geocoding_response = requests.get(geocoding_url).json()
        driver_lat = geocoding_response["results"][0]["geometry"]["location"]["lat"]
        driver_lon = geocoding_response["results"][0]["geometry"]["location"]["lng"]
        distance = haversine(origin_lat, origin_lon, driver_lat, driver_lon)
        distances.append(distance)

    # Check if there are any results
    if not distances:
        print("No drivers found.")
        return

    # Extract the name of the nearest driver within the specified distance
    min_distance = float("inf")
    min_index = -1
    for i, distance in enumerate(distances):
        if distance < min_distance and distance < max_distance:
            min_distance = distance
            min_index = i

    if min_index != -1:
        return driver_names[min_index], driver_ID[min_index]

    else:
        print(f"No drivers found within {max_distance} miles of the specified address.")
# =====================================
def check_for_updates():
    global last_update_time, last_result_set
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gain044298809",
        database="tracking",
    )
    cur = conn.cursor()

    # Check if there are any pending packages
    cur.execute(
        "SELECT COUNT(*) FROM package1 WHERE status = 'pending' ORDER BY timestamp DESC"
    )
    pending_count = cur.fetchone()[0]
    if pending_count == 0:
        print("No pending packages. Nothing to update.")
    else:
        # Get the latest update time from the database
        cur.execute("SELECT * FROM package1")
        result_set = cur.fetchall()

        # Compare the latest result set with the previous result set
        if result_set != last_result_set:
            # If there's been an update, toggle the function
            toggle_function(cur)
            last_result_set = result_set

            cur.execute(
                "SELECT referenceNum,origin FROM package1 WHERE status = 'pending' ORDER BY timestamp DESC LIMIT 1 "
            )
            latest_row = cur.fetchone()
            package_origin = latest_row[1]
            # access the first (and only) element of the tuple
            referenceNum = latest_row[0]
            # find nearby driver
            drivername, driverid = find_nearby_driver(package_origin)
            print("============================")
            print("Reference Number: ",referenceNum)
            print("The nearby driver : ", drivername,   "\t\tID:  ", driverid)
            cur.execute("SELECT current_location FROM driver WHERE id = %s", (driverid,))
            lastest_row2 = cur.fetchone()
            driver_location = lastest_row2[0]

            print("The driver is far from origin:  ",get_distance( package_origin,driver_location), "miles",)
            print("The estimate time to pick up :  ",get_estimate( package_origin,driver_location), "minutes",)
            
            answer = input(f"Would you like to open the map ? (y/n): ")
            if answer == 'y':
                open_map(driver_location,package_origin )
            
            cur.execute("SELECT id,status FROM package1 ORDER BY status DESC LIMIT 1")
            lastest_status = cur.fetchone()
            # get the package ID from the user
            package_id = lastest_status[0]
            print("Package ID: ",package_id , "has been picked up by ",drivername)
            # check if the package exists in the database
            query = "SELECT status FROM package1 WHERE id = %s"
            cur.execute(query, (package_id,))
            result = cur.fetchone()

            if result:
                # update the status and location of the package
                query = "UPDATE package1 SET status = 'in progress', location = %s WHERE id = %s"

                # This address will replace with the driver go to
                print("===========================================")
                location= "Wayne, NJ 07470"
              
                cur.execute(query, (location, package_id))
                conn.commit()
                #check what location looklike
                print("===========================================")
                print("Package status and location updated successfully.")
            else:
                print("Package not found in the database.")

        # Close the database connection
        cur.close()
        conn.close()
# =====================================
def toggle_function(cur):
    # Your code to toggle the function goes here

    print("\t\t\t", "=" * 32)
    print("\t\t\t", "|{:^30s}|".format("Report"))
    print("=" * 70)

    col_widths = [15, 40, 15]

    # Print the table header
    # Define the header and column widths
    header = ["ReferenceNumbe", "Name", "Location", "Status"]
    col_widths = [15, 25, 35, 10]

    # Build the header string
    header_str = ""
    for i, col in enumerate(header):
        header_str += f"{col:{col_widths[i]}} | "

    header_str = header_str[:-3]  

    # Print the header and separator line
    print(header_str)
    print("=" * sum(col_widths))

    # Execute the SQL query
    query = (
        "SELECT ReferenceNum, Name, Location, Status FROM package1 WHERE status = %s"
    )
    status = "pending"
    cur.execute(query, (status,))

    # Print the rows
    for row in cur.fetchall():
        row_str = ""
        for i, col in enumerate(row):
            row_str += f"{str(col):{col_widths[i]}} | "
        row_str = row_str[:-3] 
        print(row_str)


