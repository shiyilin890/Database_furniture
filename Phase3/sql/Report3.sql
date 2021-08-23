SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

SELECT Store.storeID AS `Store ID`, Store.street_address AS `Store address`, City.city_name AS `City name`, YEAR(Sold.date_attr) AS `Sales year`, SUM(IF(Sold.PID = Discount.PID AND Sold.date_attr = Discount.date_attr, Discount.discount_price, Product.retail_price)
* Sold.quantity) AS `Total revenue`
FROM Sold
LEFT OUTER JOIN Discount ON Sold.PID = Discount.PID AND Sold.date_attr = Discount.date_attr, Store, City, Product
WHERE Sold.storeID = Store.storeID AND Store.city_name = City.city_name AND City.state = '$state' AND  Sold.PID = Product.PID
GROUP BY Store.storeID, `Sales year`
ORDER BY `Sales year`, `Total revenue` DESC;