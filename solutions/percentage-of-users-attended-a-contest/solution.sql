# Write your MySQL query statement below
-- select contest_id, round(sum(case when 1=1 then 1 else 0 end)/(select count(*) from Users),2) as percentage 
-- from Register r join Users u 
-- on r.user_id = u.user_id order by percentage desc,contest_id asc;

-- select contest_id,  as percentage
-- from (select distinct r.contest_id,u.user_id from Register r cross join Users u)

select contest_id, round((sum(case when 1=1 then 1 else 0 end)/(select count(user_id) from Users)*100),2) as percentage 
from Register 
group by contest_id 
order by percentage desc, contest_id;