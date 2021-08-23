SELECT 
    MONTHS.`Month`,
    IFNULL(smallCategory, 0) AS `No Childcare Service`,
    IFNULL(mediumCategory, 0) AS `Short Childcare Service`,
    IFNULL(LargeCategory, 0) AS `Long Childcare Service`,
    IFNULL(extraLargeCategory, 0) AS `Full Childcare Service`
FROM
    (SELECT DISTINCT MONTH(sold.date_attr) AS `MONTH` From sold) AS MONTHS 
	    LEFT JOIN
		(SELECT 
			Month(Sold.date_attr) AS `Month`,
            SUM(quantity * IF(ISNULL(Discount.discount_price), Product.retail_price, Discount.discount_price)) AS `smallCategory`
		FROM Sold 
		JOIN Product ON Product.PID = Sold.PID
		JOIN Store ON Store.storeID = Sold.storeID AND Store.childcare_limit = '0'
		LEFT OUTER JOIN Discount ON Sold.date_attr = Discount.date_attr AND Sold.PID = Discount.PID
		GROUP BY Month(Sold.date_attr)) AS SMALL ON MONTHS.`Month` = SMALL.`Month` 
LEFT JOIN
		(SELECT 
			Month(Sold.date_attr) AS `Month`,
            SUM(quantity * IF(ISNULL(Discount.discount_price), Product.retail_price, Discount.discount_price)) AS `mediumCategory`
		FROM Sold 
		JOIN Product ON Product.PID = Sold.PID
		JOIN Store ON Store.storeID = Sold.storeID AND Store.childcare_limit = '30'
		LEFT OUTER JOIN Discount ON Sold.date_attr = Discount.date_attr AND Sold.PID = Discount.PID
		GROUP BY Month(Sold.date_attr)) AS MEDIUM1 ON MONTHS.`Month` = MEDIUM1.`Month` 
LEFT JOIN
		(SELECT 
			Month(Sold.date_attr) AS `Month`,
            SUM(quantity * IF(ISNULL(Discount.discount_price), Product.retail_price, Discount.discount_price)) AS `largeCategory`
		FROM Sold 
		JOIN Product ON Product.PID = Sold.PID
		JOIN Store ON Store.storeID = Sold.storeID AND Store.childcare_limit = '45'
		LEFT OUTER JOIN Discount ON Sold.date_attr = Discount.date_attr AND Sold.PID = Discount.PID
		GROUP BY Month(Sold.date_attr)) AS LARGE ON MONTHS.`Month` = LARGE.`Month` 
LEFT JOIN
		(SELECT 
			Month(Sold.date_attr) AS `Month`,
            SUM(quantity * IF(ISNULL(Discount.discount_price), Product.retail_price, Discount.discount_price)) AS `extraLargeCategory`
		FROM Sold 
		JOIN Product ON Product.PID = Sold.PID
		JOIN Store ON Store.storeID = Sold.storeID AND Store.childcare_limit = '60'
		LEFT OUTER JOIN Discount ON Sold.date_attr = Discount.date_attr AND Sold.PID = Discount.PID
		GROUP BY Month(Sold.date_attr)) AS EXTRALARGE ON MONTHS.`Month` = EXTRALARGE.`Month` ;