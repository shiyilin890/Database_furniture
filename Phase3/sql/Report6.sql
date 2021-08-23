SELECT
	YEARS.`Year`,
    IFNULL(smallCategory, 0) AS `Small City`,
	IFNULL(mediumCategory, 0) AS `Medium City`,
	IFNULL(largeCategory, 0) AS `Large City`,
	IFNULL(extraLargeCategory, 0) AS `Extra Large City`
FROM
	(SELECT DISTINCT YEAR(Sold.date_attr) AS `Year` FROM Sold) AS YEARS
    LEFT JOIN
		(SELECT 
			YEAR(Sold.date_attr) AS `Year`,
            SUM(quantity * IF(ISNULL(Discount.discount_price), Product.retail_price, Discount.discount_price)) AS `smallCategory`
		FROM Sold 
		JOIN Product ON Product.PID = Sold.PID
		JOIN Store ON Store.storeID = Sold.storeID
		JOIN City ON City.city_name = Store.city_name AND City.state = Store.state AND City.population < 3700000
		LEFT OUTER JOIN Discount ON Sold.date_attr = Discount.date_attr AND Sold.PID = Discount.PID
		GROUP BY YEAR(Sold.date_attr)) AS SMALL ON YEARS.`Year` = SMALL.`Year`   
	LEFT JOIN
		(SELECT 
			YEAR(Sold.date_attr) AS `Year`,
            SUM(quantity * IF(ISNULL(Discount.discount_price), Product.retail_price, Discount.discount_price)) AS `mediumCategory`
		FROM Sold 
		JOIN Product ON Product.PID = Sold.PID
		JOIN Store ON Store.storeID = Sold.storeID
		JOIN City ON City.city_name = Store.city_name AND City.state = Store.state AND City.population >= 3700000 AND City.population < 6700000
		LEFT OUTER JOIN Discount ON Sold.date_attr = Discount.date_attr AND Sold.PID = Discount.PID
		GROUP BY YEAR(Sold.date_attr)) AS MEDIUM ON YEARS.`Year` = MEDIUM.`Year`   
	LEFT JOIN
		(SELECT 
			YEAR(Sold.date_attr) AS `Year`,
            SUM(quantity * IF(ISNULL(Discount.discount_price), Product.retail_price, Discount.discount_price)) AS `largeCategory`
		FROM Sold 
		JOIN Product ON Product.PID = Sold.PID
		JOIN Store ON Store.storeID = Sold.storeID
		JOIN City ON City.city_name = Store.city_name AND City.state = Store.state AND City.population >= 6700000 AND City.population < 9000000
		LEFT OUTER JOIN Discount ON Sold.date_attr = Discount.date_attr AND Sold.PID = Discount.PID
		GROUP BY YEAR(Sold.date_attr)) AS LARGE ON YEARS.`Year` = LARGE.`Year`   
	LEFT JOIN
		(SELECT
			YEAR(Sold.date_attr) AS `Year`, 
			SUM(quantity * IF(ISNULL(Discount.discount_price), Product.retail_price, Discount.discount_price)) AS `extraLargeCategory`
		FROM Sold
		JOIN Product ON Product.PID = Sold.PID
		JOIN Store ON Store.storeID = Sold.storeID
		JOIN City ON City.city_name = Store.city_name AND City.state = Store.state AND City.population >= 9000000
		LEFT OUTER JOIN Discount ON Sold.date_attr = Discount.date_attr AND Sold.PID = Discount.PID
		GROUP BY YEAR(Sold.date_attr)) AS EXTRALARGE ON YEARS.`Year` = EXTRALARGE.`Year`
		ORDER BY Years.`Year`;
