
CREATE TABLE package1 (
  id INT PRIMARY KEY AUTO_INCREMENT,
  referenceNum VARCHAR(255),
  name VARCHAR(255),
  weight DECIMAL(4,1),
  types VARCHAR(255),
  size VARCHAR(255),
  origin VARCHAR(255),
  destination VARCHAR(255),
  pickup_time VARCHAR(255),
  status VARCHAR(255),
  location VARCHAR(255),
  rating INT
);

INSERT INTO package1 (referenceNum, name, weight, types, size, origin, destination, pickup_time, status, location) 
VALUES ('123456', 'William Paterson University', 5.6, 'document', '4x4x3', '300 Pompton Rd, Wayne, NJ 07470, United States', '1 College Boulevard, Paterson, NJ 07505, United States', '7:00am', 'pending', '300 Pompton Rd, Wayne, NJ 07470, United States');

INSERT INTO package1 (referenceNum, name, weight, types, size, origin, destination, pickup_time, status, location) 
VALUES ('789012', 'Passaic County Community College: Wanaque Campus', 3.2, 'package', '12x8x6', '500 Union Avenue, Wanaque, NJ 07465, United States', '1 College Boulevard, Paterson, NJ 07505, United States', '7:00pm', 'pending', '500 Union Avenue, Wanaque, NJ 07465, United States');

select * from package1;

CREATE TABLE driver (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  current_location VARCHAR(255),
  status VARCHAR(255),
  destination VARCHAR(255)
);

-- Insert 5 rows into the driver table
INSERT INTO driver (name, current_location, status, destination) VALUES
('John', '2050 Hamburg Tpke, Wayne, NJ 07470', 'available', '181 US-46, Totowa, NJ 07512'),
('Mary', '550 Ramapo Valley Rd, Oakland, NJ 07436', 'on break', '219 Paterson Ave, Little Falls, NJ 07424'),
('David', '1490 NJ-23, Wayne, NJ 07470', 'delivering', '7 Wanaque Ave, Pompton Lakes, NJ 07442'),
('Emma', '8-12 Main St, Little Falls, NJ 07424', 'available', '242 Union Blvd, Totowa, NJ 07512'),
('Michael', '29 Wanaque Ave, Pompton Lakes, NJ 07442', 'available', '16 Willowbrook Blvd, Wayne, NJ 07470');


select * from package1;





