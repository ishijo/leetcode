# Write your MySQL query statement below
with cte as (select * from Orders where date_format(order_date,'%Y-%m')='2020-02') 
select p.product_name, o.units as unit 
from Products p join (select cte.product_id as product_id,sum(cte.unit) as units from cte group by cte.product_id) o on 
p.product_id = o.product_id where 
o.units>=100
 