# Write your MySQL query statement below
-- with cte as (select accepter_id, requester_id from RequestAccepted 
-- union all 
-- select requester_id, accepter_id from RequestAccepted) 
-- select accepter_id, count(requester_id) from cte

with cte as (select requester_id as id from RequestAccepted
union all
select accepter_id from RequestAccepted) 
select id, count(id) as num 
from cte 
group by id 
order by count(id) desc 
limit 1;