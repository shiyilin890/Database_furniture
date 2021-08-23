SELECT 
	Category.category_name AS `Category Name`, 
	COUNT(Product.PID) AS `Number of Products`,
    MIN(Product.retail_price) AS `Minimum Price`,
    AVG(Product.retail_price) AS `Average Price`,
    MAX(Product.retail_price) AS `Maximum Price`
FROM Category 
LEFT JOIN BelongTo 
ON Category.category_name = BelongTo.category_name
LEFT JOIN Product
ON Product.PID = BelongTo.PID
GROUP BY `Category Name`
ORDER BY `Category Name` ASC;