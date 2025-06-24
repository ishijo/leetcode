# Write your MySQL query statement below
with cte as (
    Select delivery_id, customer_id, order_date, customer_pref_delivery_date ,
row_number() over(partition by customer_id order by order_date) as order_day_num 
from Delivery 
)
select round(sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)*100/count(*),2) as immediate_percentage from cte where order_day_num=1;