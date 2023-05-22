import tkinter as tk
import requests
from io import BytesIO
import googlemaps
from PIL import Image, ImageTk

# Set up Google Maps API client
api_key = "AIzaSyCWmC0WgvwKTS__QgP0NFkjE_Ugr7QYDhg"
gmaps = googlemaps.Client(api_key)

# Create the default root window
root = tk.Tk()

# Get directions between two locations
directions_result = gmaps.directions(
    "191 Overmount ave, woodland park, nj , 07424",
    "300 Pompton Rd, Wayne, NJ 07470, United States",
    mode="driving",
)

# Get the polyline of the directions and format it for the Google Maps Static API
polyline = directions_result[0]["overview_polyline"]["points"]
path = f"weight:3%7Ccolor:blue%7Cenc:{polyline}"

# Get the image of the map from the Google Maps Static API
url = f"https://maps.googleapis.com/maps/api/staticmap?size=640x480&path={path}&key={api_key}"
response = requests.get(url)
image_data = response.content

# Open the image using the PIL library


image = Image.open(BytesIO(image_data))

# Convert the image to a PhotoImage object that can be used with tkinter
photo = ImageTk.PhotoImage(image)

# Create a label with the image
label = tk.Label(root, image=photo)
label.pack()

# Start the tkinter event loop
root.mainloop()
