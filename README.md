# UPS-Project-PSUEDOCODE

# Initialize the application with the following parameters:
- Create the package information
   This will use the dictionary method (name,weight,size,originalpoint,destinationpoint,pickuptime,)

   'name': 'Gain mullane',
    'weight': random.randint(1, 100) / 10 ,
    'types': 'document',
    'size': '4x4x3',
    'origin_pickup_points' : office_A,
    'destination_pickup_points' : office_B,
    'pickup_time' : '7:00am',
    'status':status.status,
    'location': 'address'
- Reusable package inventory (check to see if there is a reusable package that is going to be used.  We will create the reusable package)

# While the application is running:
Create schedulepickup function
-para (time, originpoint,destinationpoint)
-check if time is it the pickup normal our or urgent hour
-update the status to “shipped”
-check where is the nearest pickup ups store - might need to crate another function
-check how far from origin —> ups store        this will: update the mileage in package1
-calculate the time estimate time to delivery package to destination point (origin —> ups store —> ups main facility   ) 
    Return : status, mileage, estimatime derivery
- Update the package's 1Z shipment numbers and store them in the database for future reference

# When a customer wants to track their package:
-Create tracking function
-this function will ask the user to input the ref number or tracking number 
If it == refnum or 1z shipment label it will return the information about the package in to the html
- Retrieve the package's status and update the customer on its current location and estimated delivery time (    information will go out as html

# When a package has been delivered:
If the package has been the delivery when the user input the tracking number and status show that it’s delivered , 
-prompt pop up that ask the user to rate the system 1-5 star and also write the review if they want.  This will store in the database 
Refname: rate 🙂










To ensure package safety and reusability:
- Regularly inspect the reusable packages for damage and replace as needed  (   
- Maintain records of package usage and mileage to ensure they are retired before they become unusable




