DROP VIEW IF EXISTS soldin;
CREATE VIEW soldin AS 
SELECT s.PID, p.product_name,
SUM(s.quantity) AS soldincamp
FROM 
(Sold s
JOIN HasAdCamp c
ON s.date_attr = c.date_attr
) 
JOIN Product p
ON s.PID = p.PID
GROUP BY s.PID
order by s.PID;

DROP VIEW IF EXISTS soldout;
CREATE VIEW soldout AS
SELECT ss.PID, pp.product_name,
SUM(ss.quantity) AS soldoutcamp
FROM 
(
Sold ss
JOIN Product pp
ON ss.PID = pp.PID
)
LEFT JOIN HasAdCamp cc USING (date_attr)
WHERE cc.date_attr IS NULL
GROUP BY ss.PID
order by ss.PID;

DROP VIEW IF EXISTS diff1;
create view diff1 as
select soldout.*, soldin.soldincamp from 
soldout
left outer join
soldin
on soldin.pid=soldout.pid;

DROP VIEW IF EXISTS diff;
create view diff as
select *, COALESCE(diff1.soldincamp,0) as si, COALESCE(diff1.soldoutcamp,0) as so from diff1;

select * from (
select pid, product_name, si, so, (si-so) as difference
from diff
order by difference DESC
limit 10
)as top
union all
select * from (
select pid, product_name, si, so, (si-so) as difference
from diff
order by difference 
limit 10
)as btm;