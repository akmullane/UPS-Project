import requests
import datetime
import json

#=====================================
def getDistance(origin,destination):
    UPS_Store = findNearbyStore(origin)
    # Call the Google Maps Distance Matrix API to get the travel time and distance
    api_key ="AIzaSyCWmC0WgvwKTS__QgP0NFkjE_Ugr7QYDhg"  
    # Replace with your own API key
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={origin}&destinations={UPS_Store}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    distance1 = float(data['rows'][0]['elements'][0]['distance']['text'].split(' ')[0])



    url2 = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={UPS_Store}&destinations={destination}&key={api_key}"
    response2 = requests.get(url2)
    data2 = response2.json()
    distance2 = float(data2['rows'][0]['elements'][0]['distance']['text'].split(' ')[0])

    return distance1+distance2
#=====================================
def getEstimate(origin,destination):
    UPS_store=findNearbyStore(origin)
    # Call the Google Maps Distance Matrix API to get the travel time and distance
    api_key ="AIzaSyCWmC0WgvwKTS__QgP0NFkjE_Ugr7QYDhg"  
    # Replace with your own API key
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={origin}&destinations={UPS_store}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    travel_time =  float(data['rows'][0]['elements'][0]['distance']['text'].split(' ')[0])


    url2 = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={UPS_store}&destinations={destination}&key={api_key}"
    response2 = requests.get(url2)
    data2 = response2.json()
    travel_time2 =  float(data2['rows'][0]['elements'][0]['distance']['text'].split(' ')[0])

    print(travel_time)
    print(travel_time2)
    return travel_time+travel_time2
#=====================================
def schedule_pickup(time):

    # Normal Hour Pickups:
    # Pickup frequency: Once per window
    normal_hour_pickups = ("7:00am", "7:00pm")

    # Urgent Hour Pickups:
    # Pickup window: 7:00am to 5:00pm
    # Pickup frequency: Every 10 minutes
    urgent_hour_pickups = ("7:00am", "7:10am", "7:20am", "7:30am", "7:40am", "7:50am", "8:00am", "8:10am", "8:20am", "8:30am", "8:40am", "8:50am", "9:00am", "9:10am", "9:20am", "9:30am", "9:40am", "9:50am", "10:00am", "10:10am", "10:20am", "10:30am", "10:40am", "10:50am", "11:00am", "11:10am", "11:20am", "11:30am", "11:40am", "11:50am", "12:00pm", "12:10pm", "12:20pm", "12:30pm", "12:40pm", "12:50pm", "1:00pm", "1:10pm", "1:20pm", "1:30pm", "1:40pm", "1:50pm", "2:00pm", "2:10pm", "2:20pm", "2:30pm", "2:40pm", "2:50pm", "3:00pm", "3:10pm", "3:20pm", "3:30pm", "3:40pm", "3:50pm", "4:00pm", "4:10pm", "4:20pm", "4:30pm", "4:40pm", "4:50pm","5:00pm")
    nearest_store = None

    # Check if pickup time falls within normal or urgent hour pickup windows
    if (time in normal_hour_pickups):
        print("Your pickup is scheduled for the normal hour window.")
    else:
        print("Your pickup is scheduled for the urgent hour window.")
    return "shipped"
#==========================================
def print_package(package):
    print(f"Name: {package.name}")
    print(f"Weight: {package.weight}")
    print(f"Types: {package.types}")
    print(f"Size: {package.size}")
    print(f"Origin: {package.origin}")
    print(f"Destination: {package.destination}")
    print(f"Pickup Time: {package.pickup_time}")
    print(f"Status: {package.status}")
    print(f"Location: {package.location}")
    print(f"Reference Number: {package.referenceNum}")
    print(f"Estimate time: {package.estimate} minutes")
    print(f"Mileage: {package.mileage} miles")

#==========================================
def findNearbyStore(origin):
    API_KEY = 'AIzaSyCWmC0WgvwKTS__QgP0NFkjE_Ugr7QYDhg'
    address = origin

    # Use the Geocoding API to get the latitude and longitude of the address
    geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}'
    geocoding_response = requests.get(geocoding_url).json()
    latitude = geocoding_response['results'][0]['geometry']['location']['lat']
    longitude = geocoding_response['results'][0]['geometry']['location']['lng']

    # Use the Places API to search for UPS stores near the address
    places_url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius=5000&type=store&keyword=UPS&fields=name,vicinity,formatted_address&key={API_KEY}'
    places_response = requests.get(places_url).json()

    # Check if there are any results
    if 'results' not in places_response:
        print("Error: No results found in API response.")
        print(json.dumps(places_response, indent=2))
        exit()

    # Extract the name and address of the nearest UPS store
    if len(places_response['results']) > 0:
        nearest_store = places_response['results'][0]
        if 'formatted_address' in nearest_store:
            store_address = nearest_store['formatted_address']
        elif 'vicinity' in nearest_store:
            store_address = nearest_store['vicinity']
        else:
            store_address = "Unknown"
        store_name = nearest_store['name']
    #     print(f"The nearest UPS store to {address} is {store_name} at {store_address}.")
    else:
        print("No UPS stores found within 5000 meters of the specified address.")
    return store_address                 
#===============================================
def print_html(package):
    html = f"""
    <html>
    <body>
        <h1>{package.name}</h1>
        <ul>
        <li>Weight: {package.weight}</li>
        <li>Types: {package.types}</li>
        <li>Size: {package.size}</li>
        <li>Origin: {package.origin}</li>
        <li>Destination: {package.destination}</li>
        <li>Pickup Time: {package.pickup_time}</li>
        <li>Status: {package.status}</li>
        <li>Location: {package.location}</li>
        <li>Reference Number: {package.referenceNum}</li>
        <li>Estimate time: {package.estimate} minutes</li>
        <li>Mileage: {package.mileage} miles</li>
        </ul>
    </body>
    </html>
"""
    # Write the HTML code to a file
    with open("output.html", "w") as file:
        file.write(html)


