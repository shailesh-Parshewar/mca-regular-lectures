use company_db;

create table Employees4 (empId Int primary key, firstname varchar(10), lastname varchar(10), empAge int, salary int);

-- applying check on single column
alter table Employees4 add check(salary >= 5000);

-- applying check on multiple columns. You need to give it a name so it can identify it later on 
alter table Employees4 add constraint check_salary_age check(salary > 15000 and empAge > 18);

desc Employees4;
-- command to check how the table was created
-- this returns create table command you'd need to recreate the exact table
-- this doesn't account for history of changes, just the latest state of table0
show create table Employees4;


insert into Employees4 values(1, "Shailesh", "Parshewar", 23, 21000);

-- command to drop check constraint table
-- to drop a constraint you need to give the engine the constraint name, you cannot drop constraints based on column. 
-- this might be to avoid the behaviour of accidentally dropping multiple constraints if it was based on column name only.
-- a single constraint can be applied on more than one column, and a single column can have more than one constraints,
-- this many to many relation betweeen column and constraints make it difficult to identify the right thing to delete. 
alter table Employees4 drop check check_salary_age;