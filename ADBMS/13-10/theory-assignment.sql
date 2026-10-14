create database companyDB;
use companyDB;

create table Employees (EmpID int primary key, EmpName varchar(50), salary int, joinDate date);
DESC Employees;

CREATE TABLE Departments (DeptID INT PRIMARY KEY, DeptName VARCHAR(50));
DESC Departments;

ALTER TABLE Employees ADD COLUMN email VARCHAR(100);
ALTER TABLE Departments ADD COLUMN Dept_location VARCHAR(200);

ALTER TABLE Employees ADD COLUMN Phone INT NOT NULL;

ALTER TABLE Employees MODIFY COLUMN EmpName VARCHAR(100);

ALTER TABLE Departments DROP PRIMARY KEY;
DESC Departments;
DESC Employees;
ALTER TABLE Employees ADD COLUMN DeptID INT NOT NULL;
ALTER TABLE Employees ADD CONSTRAINT fk_dept_id FOREIGN KEY (DeptID) REFERENCES Departments(DeptID);

ALTER TABLE Employees RENAME COLUMN EmpName TO EmployeeName;
ALTER TABLE Employees ADD COLUMN EmpAge INT;
ALTER TABLE Employees ADD CONSTRAINT chk_salary_and_age CHECK(EmpAge > 18 and salary > 15000);
insert into departments values (1, "data-assets", "pune");
INSERT INTO EmployeeDetails VALUES (1, "shailesh",21000,'2021-10-10', "shailesh@email.com", 1, 17);
INSERT INTO EmployeeDetails VALUES (2, "shailesh",12000,'2021-10-10', "shailesh@email.com", 1, 21);

ALTER TABLE Employees DROP COLUMN Phone;

RENAME TABLE Employees TO EmployeeDetails;
SHOW TABLES;

ALTER TABLE EmployeeDetails DROP CONSTRAINT chk_salary_and_age;

DROP TABLE Departments;
DROP DATABASE CompanyDb;

Show databases;