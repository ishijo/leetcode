# Write your MySQL query statement below
with cte as (select product_id, year, rank() over(partition by product_id order by year) as rn, quantity, price from Sales) 
select product_id, year as first_year,quantity, price from cte where rn = 1