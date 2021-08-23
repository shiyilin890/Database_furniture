SELECT COUNT(storeID) AS num_store
FROM Store;

SELECT COUNT(storeID) AS num_storefood
FROM Store
WHERE has_restaurant = 1 OR has_snack_bar = 1;

SELECT COUNT(storeID) AS num_childcare
FROM Store
WHERE childcare_limit != '0';

SELECT COUNT(PID) AS num_product
FROM Product;

SELECT COUNT(camp_description) AS num_camp
FROM AdCamp;


SELECT 1
FROM holiday
WHERE holiday_name = 'Easter2020';

INSERT INTO holiday (holiday_name, date_attr) VALUES ('name', 'time');


SELECT population
FROM City
WHERE city_name = 'Austin' AND state = 'TX';

UPDATE City SET population = 8100000 WHERE city_name = 'Austin' AND state = 'TX';