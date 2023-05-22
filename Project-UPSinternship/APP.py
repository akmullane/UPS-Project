from flask import Flask, jsonify, render_template, request
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost", user="root", password="Gain044298809", database="tracking"
)
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("tracking.html")


@app.route("/rating")
def get_rating():
    return render_template("rating.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


@app.route("/get_tracking_info", methods=["POST"])
def get_tracking_info():
    trackingNumber = request.form["trackingNumber"]
    # Retrieve package information from database
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT * FROM package1 WHERE referenceNum = %s", (trackingNumber,)
    )
    row = mycursor.fetchone()
    if row is None:
        return render_template("trackingNotFound.html")
    package_info = {
        "ReferenceNumber": row[1],
        "Name": row[2],
        "Weight": row[3],
        "Types": row[4],
        "Size": row[5],
        "Origin": row[6],
        "Destination": row[7],
        "PickupTime": row[8],
        "Status": row[9],
        "Location": row[10]
        # Add other package information fields here
    }
    return render_template("packingInfo.html", package_info=package_info)

if __name__ == "__main__":
    app.run(debug=True)

