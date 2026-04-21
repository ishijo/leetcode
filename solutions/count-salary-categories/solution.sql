# Write your MySQL query statement below
with cte1 as (select account_id, case when income<20000 then "Low Salary" 
                        when income>=20000 and income<=50000 then "Average Salary" 
                        when income>50000 then "High Salary" end as category, income 
from Accounts ),
cte2 as (select "Low Salary" as category
            union
            select "Average Salary"
            union
            select "High Salary") 
select cte2.category as category, count(cte1.account_id) as accounts_count from 
cte2 left join cte1 on 
cte2.category = cte1.category 
group by cte2.category