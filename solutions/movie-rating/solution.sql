# Write your MySQL query statement below
with cte1 as (select Users.user_id, Movies.movie_id, MovieRating.rating, Movies.title, Users.name, MovieRating.created_at from 
MovieRating join Movies join Users on 
MovieRating.movie_id = Movies.movie_id and MovieRating.user_id = Users.user_id),
cte2 as (select movie_id,title,avg(rating) as avg_rating from cte1 where date_format(created_at,'%Y-%m')='2020-02' group by movie_id, title order by avg_rating desc, title asc limit 1),
cte3 as (select user_id, name, count(movie_id) as num_movies from cte1 group by user_id, name order by num_movies desc, name asc  limit 1) 
select cte3.name as results from cte3 
union all
select cte2.title from cte2 
