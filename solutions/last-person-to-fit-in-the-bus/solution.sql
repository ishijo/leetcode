# Write your MySQL query statement below
with cte as (select 
*, sum(weight) over(order by turn) as cum_sum
from Queue 
order by turn)

select distinct first_value(person_name) over(order by turn desc) as person_name from cte where cum_sum<=1000

