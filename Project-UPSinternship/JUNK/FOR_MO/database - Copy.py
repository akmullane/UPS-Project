import mysql.connector
from JUNK.package import Package
import random
import ALL

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Gain044298809", database="tracking"
)
print("\t\t\t", "=" * 32)
print("\t\t\t", "|{:^30s}|".format("Report"))
print("=" * 70)


col_widths = [15, 40, 15]
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM driver")
myresult = mycursor.fetchall()

# Print the table header
header = ["Name", "Current Location", "Status"]
header_str = f"{header[0]} \t\t| {header[1]}\t                     | {header[2]}"
print(header_str)
print("=" * 70)
# Print the table
for row in myresult:
    name1 = row[1]
    currentLocation = row[2]
    status = row[3]
    row_str = [name1, currentLocation, status]
    for i, col in enumerate(row_str):
        row_str[i] = f"{col:{col_widths[i]}}"
    print(" | ".join(row_str))


print(
    "The nearby package 1 : ",
    ALL.findNearbyDriver("300 Pompton Rd, Wayne, NJ 07470, United States"),
)
print(
    "The driver is far from origin:  ",
    ALL.getDistance(
        "1490 NJ-23, Wayne, NJ 07470", "300 Pompton Rd, Wayne, NJ 07470, United States"
    ),
    "miles",
)
print(
    "Estimate time:  ",
    ALL.getEstimate2(
        "1490 NJ-23, Wayne, NJ 07470", "300 Pompton Rd, Wayne, NJ 07470, United States"
    ),
    "minutes",
)
print("=================================")
mycursor2 = mydb.cursor()
mycursor2.execute("SELECT * FROM package1")
myresult = mycursor2.fetchall()

# for row in myresult:
#     name = row[0]
#     weight = row[1]
#     location = row[2]
#     print(name, "|", weight, "|", location, "|")
