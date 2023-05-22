import os
import requests
import json
import mysql.connector
import math

api_key = "YOUR API"

# =====================================
def getDistance(origin, destination):
    UPS_Store = findNearbyStore(origin)
    # Call the Google Maps Distance Matrix API to get the travel time and distance
    # Replace with your own API key
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={origin}&destinations={UPS_Store}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    distance1 = float(data["rows"][0]["elements"][0]["distance"]["text"].split(" ")[0])

    url2 = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={UPS_Store}&destinations={destination}&key={api_key}"
    response2 = requests.get(url2)
    data2 = response2.json()
    distance2 = float(data2["rows"][0]["elements"][0]["distance"]["text"].split(" ")[0])

    return distance1 + distance2


# =====================================
def getEstimate(origin, destination):
    UPS_store = findNearbyStore(origin)
    # Call the Google Maps Distance Matrix API to get the travel time and distance
    # Replace with your own API key
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={origin}&destinations={UPS_store}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    travel_time = float(
        data["rows"][0]["elements"][0]["distance"]["text"].split(" ")[0]
    )

    url2 = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={UPS_store}&destinations={destination}&key={api_key}"
    response2 = requests.get(url2)
    data2 = response2.json()
    travel_time2 = float(
        data2["rows"][0]["elements"][0]["distance"]["text"].split(" ")[0]
    )

    print(travel_time)
    print(travel_time2)
    return travel_time + travel_time2


# =====================================
def schedule_pickup(time):
    # Normal Hour Pickups:
    # Pickup frequency: Once per window
    normal_hour_pickups = ("7:00am", "7:00pm")

    # Urgent Hour Pickups:
    # Pickup window: 7:00am to 5:00pm
    # Pickup frequency: Every 10 minutes
    urgent_hour_pickups = ("7:00am", "7:00pm")
    nearest_store = None

    # Check if pickup time falls within normal or urgent hour pickup windows
    if time in normal_hour_pickups:
        print("Your pickup is scheduled for the normal hour window.")
    else:
        print("Your pickup is scheduled for the urgent hour window.")
    return "shipped"


# =====================================
# =====================================
def findNearbyStore(origin):
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
def getEstimate2(origin, destination):
    # Call the Google Maps Distance Matrix API to get the travel time and distance
    # Replace with your own API key
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={origin}&destinations={destination}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    travel_time = float(
        data["rows"][0]["elements"][0]["distance"]["text"].split(" ")[0]
    )
    return travel_time


# =====================================
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


def findNearbyDriver(origin, max_distance=10):
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="Gain044298809", database="tracking"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM driver")

    driver_addresses = []
    myresult1 = mycursor.fetchall()
    for row in myresult1:
        driver_addresses.append(row[2])

    driver_names = []
    for row in myresult1:
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
        print(f"No drivers found.")
        return

    # Extract the name of the nearest driver within the specified distance
    min_distance = float("inf")
    min_index = -1
    for i, distance in enumerate(distances):
        if distance < min_distance and distance < max_distance:
            min_distance = distance
            min_index = i

    if min_index != -1:
        driver_name = driver_names[min_index]
        return driver_name
    else:
        print(f"No drivers found within {max_distance} miles of the specified address.")
