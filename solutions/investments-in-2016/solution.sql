# Write your MySQL query statement below
with cte1 as (select pid, lat, lon, count(*) over(partition by lat, lon) as same_city_count from Insurance),
cte2 as (select pid, tiv_2015, count(*) over(partition by tiv_2015) as same_policy_count from Insurance) 
select round(sum(tiv_2016),2) as tiv_2016
from Insurance join cte1 join cte2 
on Insurance.pid = cte1.pid and Insurance.pid = cte2.pid 
where same_city_count=1 and same_policy_count>1