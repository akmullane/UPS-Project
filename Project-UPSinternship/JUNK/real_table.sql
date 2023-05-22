use tracking;
select * from driver;
select * from package1;
drop table package1;
#=======================================================
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
  rating INT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO package1 (referenceNum, name, weight, types, size, origin, destination, pickup_time, status, location) 
VALUES ('123456', 'William Paterson University', 5.6, 'document', '4x4x3', '300 Pompton Rd, Wayne, NJ 07470, United States', '1 College Boulevard, Paterson, NJ 07505, United States', '7:00am', 'pending', '300 Pompton Rd, Wayne, NJ 07470, United States'),
('789012', 'Passaic County Community College: Wanaque Campus', 3.2, 'package', '12x8x6', '500 Union Avenue, Wanaque, NJ 07465, United States', '1 College Boulevard, Paterson, NJ 07505, United States', '7:00pm', 'pending', '500 Union Avenue, Wanaque, NJ 07465, United States');

select * from package1;
INSERT INTO package1 (referenceNum, name, weight, types, size, origin, destination, status, location) 
VALUES ('234567', '44 Rifle Camp Rd, Woodland Park, NJ 07424', 5.6, 'document', '4x4x3', '44 Rifle Camp Rd, Woodland Park, NJ 07424', '1 College Boulevard, Paterson, NJ 07505, United States', 'pending', '44 Rifle Camp Rd, Woodland Park, NJ 07424');

delete from package1;
