use world;
CREATE TABLE test (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  column_name VARCHAR(50),
  address VARCHAR(100),
  update_time TIMESTAMP
);
INSERT INTO test (id, name, column_name, address, update_time)
VALUES 
(1, 'John', 'Column1', '123 Main St', '2023-05-14 10:30:00'),
(2, 'Jane', 'Column2', '456 Elm St', '2023-05-14 11:00:00'),
(3, 'Bob', 'Column3', '789 Oak St', '2023-05-14 12:30:00'),
(4, 'Mary', 'Column4', '321 Maple St', '2023-05-14 13:00:00'),
(5, 'David', 'Column5', '654 Pine St', '2023-05-14 14:30:00');
ALTER TABLE test
DROP COLUMN column_name;
INSERT INTO test (id, name,  address, update_time)
VALUES 
(6, 'John',  '123 Main St', '2023-05-14 10:30:00');
UPDATE test
SET name = 'Jack'
WHERE id = 6;

