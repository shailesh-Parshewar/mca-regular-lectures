-- INDEXES in tables --
use company_db;

-- create index statement is used to create indexes in table
-- indexes are a way to efficiently locate data (speed up search queries) in table.
-- syntax : create index index_name on table_name(column_name);
 create index name_index on employees4(firstname);
 
 -- how to create indexes based on multiple columns
 create index emp_index on Employees4(empId, firstname);
 
 -- show indexes created on table
 show indexes from Employees4;
 
 -- drop index on tables
 -- syntax: drop index index_name on table_name;
 drop index name_index on Employees4;
 
 select * from Employees4;
 select * from Employees4 view firstname;