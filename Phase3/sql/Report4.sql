SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

SELECT YEAR(Sold.date_attr) AS `Sales year`, SUM(Sold.quantity) AS `Total units sold per year`, ROUND(SUM(Sold.quantity)/365, 2) AS `Avg units sold per day`, Groundhog.total_quantity_sold_on_groundhog AS `Total units sold on GroundHog Day`
FROM Sold, BelongTo,
(SELECT SUM(Sold.quantity) AS total_quantity_sold_on_groundhog, YEAR(Sold.date_attr) AS sold_year
FROM Sold, BelongTo
WHERE Sold.PID = BelongTo.PID AND BelongTo.category_name = 'Outdoor furniture' AND DATE_FORMAT(Sold.date_attr,'%m-%d') = '02-02'
GROUP BY sold_year
) AS Groundhog
WHERE Sold.PID = BelongTo.PID AND BelongTo.category_name = 'Outdoor furniture' AND Groundhog.sold_year = YEAR(Sold.date_attr)
GROUP BY `Sales year`
ORDER BY `Sales year`;