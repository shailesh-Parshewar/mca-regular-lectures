--  Transaction Control Language --

create database TCL;
use TCL;

create table orders (
order_id int primary key,
customer_name varchar(50),
status varchar(10)
);

-- by default autocommit, which means every change is automatically committed and so you cannot rollback -- 
set autocommit=0;

insert into orders values(4, "rohit", "scammed");

begin;
insert into orders values (1, "shailesh", "pending");
insert into orders values (2, "krishna", "complete");

select * from orders;
truncate table orders;
rollback;
commit;

update orders set customer_name = "raj" where order_id = 1;
rollback;

select * from orders;
begin;
savepoint sap0;
insert into orders values (5, "Raj", "dispatched"), (6, "Saurav", "pending");
savepoint sap1; 
update orders set status="delivered" where order_id = 5;
savepoint sap2;

update orders set status="dispatched" where order_id = 6;
savepoint sap3;
rollback to savepoint sap0;
rollback;
select * from orders;
