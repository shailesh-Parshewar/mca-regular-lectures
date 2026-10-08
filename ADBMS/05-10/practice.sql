-- CREATE DATABASE CompanyDB;

USE CompanyDB;

CREATE TABLE Employees (EmpID INT PRIMARY KEY, EmpName VARCHAR(50), Salary INT, JoinDate DATE);

CREATE TABLE Department (DeptID INT PRIMARY KEY, DeptName VARCHAR(50));

ALTER TABLE Employees ADD Email VARCHAR(100);

ALTER TABLE Department ADD Dept_location VARCHAR(100);

ALTER TABLE Employees ADD  Phone INT;
ALTER TABLE Employees MODIFY Phone INT NOT NULL;

ALTER TABLE Employees MODIFY EmpName VARCHAR(100);

ALTER TABLE Employees ADD DeptID INT;
ALTER TABLE Employees ADD FOREIGN KEY (DeptID) REFERENCES Department (DeptID);

ALTER TABLE Department DROP PRIMARY KEY;

ALTER TABLE Employees RENAME COLUMN EmpName TO EmployeeName;

-- ALTER TABLE Employees DROP Phone;

-- ALTER TABLE EmployeeDetails RENAME Employees;

DESC Employees;
DESC Department;

-- ALTER TABLE Employees DROP FOREIGN KEY employees_ibfk_1;

-- inserting into records --
INSERT INTO Department VALUES (12, "Department of nothing", "Nowhere");
INSERT INTO Employees VALUES (8, "Rohit", 87000, "2021-04-12", 12, "rohitemail@email.com", 1325476980);
SELECT * FROM Employees;
DELETE FROM Employees WHERE EmpID = NULL;

