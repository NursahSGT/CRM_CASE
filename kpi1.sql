SELECT	COUNT(DISTINCT x.customer_id)

FROM	(
	SELECT	customer.customer_id
			,customer.membership_date::timestamp
			,MIN(orders.order_date) as first_order_date
			,EXTRACT(DAY FROM MIN(orders.order_date)-customer.membership_date::timestamp)/30 as month_duration

	FROM	orders
			JOIN customer ON customer.customer_id = orders.customer_id

	GROUP BY	customer.customer_id, customer.membership_date
) as x

WHERE	x.month_duration<=6