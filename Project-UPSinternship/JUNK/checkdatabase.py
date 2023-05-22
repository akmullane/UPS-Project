import time
import mysql.connector

last_update_time = None
last_result_set = None


def check_for_updates():
    global last_update_time, last_result_set
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gain044298809",
        database="world",
    )
    cur = conn.cursor()

    # Get the latest update time from the database
    cur.execute("SELECT * FROM test")
    result_set = cur.fetchall()

    # Compare the latest result set with the previous result set
    if result_set != last_result_set:
        # If there's been an update, toggle the function
        toggle_function(cur)
        last_result_set = result_set

    # Close the database connection
    cur.close()
    conn.close()


def toggle_function(cur):
    # Your code to toggle the function goes here

    print("\t\t\t", "=" * 32)
    print("\t\t\t", "|{:^30s}|".format("Report"))
    print("=" * 70)

    col_widths = [15, 40, 15]

    cur.execute("SELECT * FROM test")
    myresult = cur.fetchall()

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

    pass


while True:
    check_for_updates()
    print(time.sleep(10))
    # time.sleep(10)  # Sleep for 1 minute before checking again
