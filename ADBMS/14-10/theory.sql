-- DQL command -- 

create database user;
show databases;

use user;

create table customer (custId int, custName varchar(15), city varchar(10), product varchar(15), price int);
desc customer;

alter table customer add primary key (custId);

insert into customer values (1, "om", "pune", "mobile", 15000);
insert into customer values (2, "prakash", "pune", "laptop", 40000);
insert into customer values (3, "ash", "pune", "headphones", 8000);

select * from customer;
select custName, product from customer;

-- create a clone table that has all the records from original customer table
create table cloneCustomer as select * from customer;
select * from cloneCustomer;
drop table cloneCustomer;

-- select with where clause


select custName, city from customer;
select custName, city from customer where custId = 1;

select custName, product from customer where price > 14000;
select custName, product from customer where price < 16000;

select * from customer where custId = 1;

select * from customer where city = "nagpur";

-- sort the results using order by;

-- by default order by sorts in ascending order
select * from customer order by price;

-- to sort in descending order
select * from  customer order by price desc;

-- sorting based on primary key
select * from customer order by  custId;
select * from customer order by custId desc;

select * from customer order by custName;
select * from customer order by custName desc;

-- sorting based on two or more columns
select * from customer order by city, price;

-- sorting based on different order
select * from customer order by city desc, price asc;

update customer set city = "Pune" where custId = 3 and custId = 1;
alter table customer add column purchased boolean not null;
update customer set purchased = False where price < 14000;
select * from customer order by purchased desc;



-- single-row functions 
-- case conversion function
-- upper function converts column to upper case, lower converts to lower case
select lower(firstName), upper(product) from customer where custId < 3;
select upper(firstName), lower(product) from customer where custId < 3;

alter table customer rename column custName to firstName;
alter table customer add column lastName varchar(15);

update customer set lastName = "Roy" where custId = 3;


select lower(firstName), upper(lastName) from customer;

-- concat function

select concat(firstName, " ", lastName) as fullName from customer ;

-- substr and instr functions

select * from customer;

-- select substr(column, start, length) as new_column_name from customer;
select substr(firstName, 1, 3) as cut from customer;

select upper(substr(firstName, 1, 1)) as cut from customer;



-- instr
-- finds first occurance of a substr in column values
select instr(firstName, "a") as pos from customer;