SELECT
	RevenueDifferenceTable.*
FROM (    
	SELECT 
		*,
	   ABS( `ActualRevenue` - `PredictedRevenue`) AS `RevenueDifference`
	FROM (
		SELECT 
			Sold.PID,
			Product.product_name AS `ProductName`,
			retail_price AS `RetailPrice`,
			SUM(quantity) AS `TotalUnitsSold`, 
 			SUM(CASE WHEN discount_price IS NOT NULL THEN quantity ELSE 0 END) AS `TotalUnitsSoldAtDiscountPrice`,
			SUM(CASE WHEN discount_price IS NULL THEN quantity ELSE 0 END) AS `TotalUnitsSoldAtRetailPrice`,
			SUM(IFNULL(discount_price, retail_price) * quantity) AS `ActualRevenue`,
			SUM((retail_price * IF(discount_price IS NULL, quantity, quantity * 0.75))) AS `PredictedRevenue`
		 FROM Sold
		 LEFT JOIN Discount
		 ON Sold.PID = Discount.PID AND Sold.date_attr = Discount.date_attr
		 LEFT JOIN Product
		 ON Sold.PID = Product.PID
		 GROUP BY Sold.PID 
	) AS RevenueTable
) AS RevenueDifferenceTable
LEFT JOIN BelongTo
ON BelongTo.PID = RevenueDifferenceTable.PID
WHERE BelongTo.category_name = "Couches and Sofas" AND`RevenueDifference` > 5000
ORDER BY `RevenueDifference` DESC;