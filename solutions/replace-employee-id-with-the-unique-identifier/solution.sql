# Write your MySQL query statement below
-- select unique_id,name from employees inner join (
--     select id,COALESCE(unique_id,"null") as unique_id from employeeUNI
-- ) b on employees.id = b.id; 

select unique_id, name
from employees
left outer join  EmployeeUNI
on Employees.id = employeeUni.id; 