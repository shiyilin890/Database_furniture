SELECT Category, Store_Type, Quantity_sold
FROM 
	(SELECT category.category_name AS Category, store.has_restaurant AS Store_Type, sum(sold.quantity) AS Quantity_sold
		FROM sold, belongto, category, store
        WHERE sold.PID = belongto.PID AND belongto.category_name = category.category_name AND sold.storeID = store.storeID

		GROUP BY category.category_name, store.has_restaurant) AS Q1
order by category ASC;