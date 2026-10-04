-- CREATING DATABASE -- 
CREATE DATABASE Institute;
-- LISTING DATABASES --
SHOW DATABASES;
-- SWITCHING TO OUR DATABASE --
USE Institute;

-- CREATING TABLE --
CREATE TABLE Staff (staff_id INT , first_name VARCHAR(100), last_name VARCHAR(100), DOB DATE, dept_id INT);
CREATE TABLE Department (dept_id INT, dept_name VARCHAR(200), dept_location VARCHAR(300));

-- DESCRIBING TABLES --
desc Staff;
desc Department;

-- ALTERING TABLE STRUCTURE --
-- ADD COLUMNS --
ALTER TABLE Staff ADD joining_year INT;
ALTER TABLE Staff ADD location VARCHAR(200);
-- DROPPING A COLUMN --
ALTER TABLE Staff drop location;
-- ADDING MANY COLUMNING IN ONE COMMAND --
ALTER TABLE Staff ADD  (age INT, contact_num INT);

-- MODIFY COLUMNS --
ALTER TABLE Staff MODIFY last_name TEXT;
ALTER TABLE Staff MODIFY staff_id INT PRIMARY KEY;
ALTER TABLE Department ADD PRIMARY KEY (dept_id);

-- ADDING FORIEGN KEY TO A TABLE --
-- Syntax : ALTER TABLE 1sttablename ADD FOREIGN KEY (1stcolumnname) REFERENCES 2ndtablename (2ndcolumnname)
ALTER TABLE Staff ADD FOREIGN KEY (dept_id) REFERENCES Department (dept_id); 
ALTER TABLE Staff ADD CONSTRAINT fk_name_department FOREIGN KEY (dept_id) REFERENCES Department(dept_id);

-- RENAME TABLE --
-- the command below doesn't give any error even if the new name is exactly the same as before --
ALTER TABLE Staff RENAME Staff;
-- the command below gives error if both the names are same --
RENAME TABLE Staff to Staff;

-- RENAME A COLUMN IN A TABLE --
ALTER TABLE Staff RENAME COLUMN Staff_id to staff_id;
-- THIS SYNTAX IS NOT VALID : RENAME COLUMN staff_id FROM Staff to staff_id1;

-- DROP TABLE --
DROP TABLE Department;

-- DROP DATABASE -- 
DROP DATABASE Institute;