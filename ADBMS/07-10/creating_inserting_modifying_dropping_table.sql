create database College;
use College;

show databases;

create table Employees (EmpID int, FirstName varchar(10), LastName varchar(10), EmpAge int, EmpZone varchar(10));
desc Employees;

insert into Employees values (1, "Shailesh", "Parshewar", 23, "Pune");
select * from Employees;

insert into Employees(EmpID, FirstName, LastName, EmpAge, EmpZone) values (2, "Krishna", Null, 21, "Pune"), (3, "Abhishek","lahane",22, "Pune"), (3, "Saurav", "Patil", 21, Null);

insert into Employees (EmpID, FirstName,EmpAge) values (9, "Rita", 25);

update Employees set LastName = "Naveri", EmpZone = "Nashik" where FirstName = "Sita" ;

update Employees set EmpZone = "Pune" where FirstName = "Saurav";


select * from Employees;
update Employees set LastName = "Karve", EmpAge = 22, EmpZone = "Pune" where EmpID > 7;
-- update Employees set EmpAge = 22 where FirstName = "Sita", set LastName = "Deshpande" where FirstName = "Shekhar";
delete from Employees where EmpID = 3;

alter table Employees rename column LastName to lastname;

truncate table Employees;
drop table Employees;


