select * from [dbo].[2019-Nov] n
​
​
-- Count number of rows
SELECT COUNT(*) AS num_rows FROM [dbo].[2019-Nov] n;
​
​
-- Count number of NaN values in fact column
SELECT COUNT(*) FROM [dbo].[2019-Nov] d WHERE brand IS NULL OR brand = '';
​
-- Calculate min and max values of fact column
SELECT MIN(price) AS min_price, MAX(price) AS max_price FROM [dbo].[2019-Nov] n;
​
-- Find start and end dates of events
SELECT MIN(event_time) AS start_date, MAX(event_time) AS end_date FROM [dbo].[2019-Nov] n;
​
-- Count number of NaN values in category_id column
SELECT COUNT(*) AS num_nans FROM [dbo].[2019-Nov] n WHERE category_id IS null ;
​
-- Find unique product IDs and the number of times they appear in the table
SELECT product_id, COUNT(*) AS num_occurrences FROM [dbo].[2019-Nov] n GROUP BY product_id order by num_occurrences desc;
​
-- Find the top 10 most common categories and the number of times they appear in the table
SELECT category_code, COUNT(*) AS num_occurrences FROM [dbo].[2019-Nov] n GROUP BY category_code ORDER BY num_occurrences DESC;
​
-- Find the number of unique user IDs
SELECT COUNT(DISTINCT user_id) AS num_users FROM [dbo].[2019-Nov] n ;
​
--task4
​
SELECT * INTO new_table FROM [dbo].[2019-Oct]
UNION ALL
SELECT * FROM [dbo].[2019-Nov]
UNION ALL
SELECT * FROM [dbo].[2019-Dec]
UNION ALL
SELECT * FROM [dbo].[2020-Jun]
UNION ALL
SELECT * FROM [dbo].[2020-Feb];
​
​
--task 5
​
WITH events_per_type AS (
  SELECT 
    event_type, 
    COUNT(*) AS num_events,
    SUM(COUNT(*)) OVER() AS total_events
  FROM [dbo].[new_table]
  GROUP BY event_type
)
SELECT 
  event_type, 
  num_events,
  ROUND(num_events/total_events::numeric, 2) AS share_of_total
FROM events_per_type;
​
select * from [dbo].[new_table]
​
-- task 6
​
WITH brand_counts AS (
  SELECT brand, COUNT(*) AS num_purchases
  FROM [dbo].[new_table]
  WHERE event_type = 'purchase'
  GROUP BY brand
)
SELECT 
  brand, 
  num_purchases, 
  RANK() OVER (ORDER BY num_purchases DESC) AS brand_rank
FROM brand_counts
ORDER BY num_purchases DESC;
​
​
​
--task 7
​
WITH user_interactions AS (
  SELECT 
    user_id,
    COUNT(*) AS num_interactions
  FROM [dbo].[new_table]
  GROUP BY user_id
),
user_purchases AS (
  SELECT 
    user_id,
    COUNT(*) AS num_purchases
  FROM [dbo].[new_table]
  WHERE event_type = 'purchase'
  GROUP BY user_id
)
SELECT 
  [dbo].[new_table].user_id,
  COALESCE(user_purchases.num_purchases, 0) AS purchase_count,
  COALESCE(user_interactions.num_interactions, 0) AS interaction_count
FROM [dbo].[new_table]
LEFT JOIN user_purchases ON [dbo].[new_table].user_id = user_purchases.user_id
LEFT JOIN user_interactions ON [dbo].[new_table].user_id = user_interactions.user_id
GROUP BY [dbo].[new_table].user_id, user_purchases.num_purchases, user_interactions.num_interactions;
​
​
​
--task8
​
SELECT event_time, 
       event_type, 
       product_id, 
       category_id, 
       category_code, 
       brand, 
       price, 
       user_id, 
       user_session, 
       100.0 * (price - LAG(price, 1) OVER (PARTITION BY user_id ORDER BY event_time))/NULLIF(LAG(price, 1) OVER (PARTITION BY user_id ORDER BY event_time), 0) AS price_increase_percent
FROM [dbo].[new_table];
​
​​
--task 9
SELECT *,
  CASE
    WHEN percent_rank() OVER (PARTITION BY user_id ORDER BY interactions) <= 0.25 THEN 1
    WHEN percent_rank() OVER (PARTITION BY user_id ORDER BY interactions) <= 0.50 THEN 2
    WHEN percent_rank() OVER (PARTITION BY user_id ORDER BY interactions) <= 0.70 THEN 3
    ELSE 4
  END AS interaction_group
FROM (
  SELECT user_id, COUNT(*) AS interactions
  FROM [dbo].[new_table]
  GROUP BY user_id
) subquery;