# Write your MySQL query statement below
with cte as (select employee_id, count(department_id) as cnt_dep from Employee group by employee_id) 
select Employee.employee_id, Employee.department_id 
from Employee join cte 
on Employee.employee_id = cte.employee_id 
where primary_flag='Y' or cnt_dep=1