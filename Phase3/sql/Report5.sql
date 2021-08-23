SELECT
	DISTINCT DATE_FORMAT(Sold.date_attr, '%M-%Y')
FROM Sold
ORDER BY
		DATE_FORMAT(Sold.date_attr, '%M-%Y') ASC;
        
SELECT Category, State, Units_Sold
FROM 
	(SELECT unitsCategory AS Category, MAX(Units_Sold) AS Units_Sold
    FROM
		(SELECT Category.category_name AS unitsCategory, City.state, SUM(quantity) AS Units_Sold
		FROM Sold
		JOIN Product ON Product.PID = Sold.PID
		JOIN Store ON Sold.storeID = Store.storeID
		JOIN City ON City.city_name = Store.city_name AND City.state = Store.state
		JOIN BelongTo ON BelongTo.PID = Sold.PID
		JOIN Category ON Category.category_name = BelongTo.category_name
		WHERE
			MONTH(Sold.date_attr) = '$month' AND YEAR(Sold.date_attr) = '$year'
		GROUP BY Category.category_name, City.state) AS Query1
	GROUP BY unitsCategory) AS Query2    
    JOIN
		(SELECT Category.category_name AS stateCategory, City.state AS State, SUM(quantity) AS stateUnits
        FROM Sold
        JOIN Product ON Product.PID = Sold.PID
		JOIN Store ON Sold.storeID = Store.storeID
		JOIN City ON City.city_name = Store.city_name AND City.state = Store.state
		JOIN BelongTo ON BelongTo.PID = Sold.PID
		JOIN Category ON Category.category_name = BelongTo.category_name
        WHERE
			MONTH(Sold.date_attr) = '$month' AND YEAR(Sold.date_attr) = '$year'
		GROUP BY Category.category_name, City.state) AS Query3 ON Category = stateCategory AND Units_Sold = stateUnits
ORDER BY Category ASC;
    