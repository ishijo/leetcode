# Write your MySQL query statement below
with cte as (select id, student,case when mod(id,2)=1 then 'swap1' else 'swap2' end as set_value 
from Seat ) 
select id, coalesce(case when set_value='swap2' then lag(student) over() else lead(student) over() end, student) as student from cte