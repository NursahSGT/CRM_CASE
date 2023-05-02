select	orders.product_id
		,orders.main_category
		,count(distinct orders.order_id) as order_count
		,sum(orders.order_amount) as order_sum
		,sum(orders.order_amount)/count(distinct orders.order_id) as avg_order_sum
		,count(distinct orders.customer_id) as customer_count
		,sum(orders.order_amount)/count(distinct orders.customer_id) as avg_customer_order_sum
		,min(orders.order_date) as first_order_date
		,max(orders.order_date) as last_order_date

from	orders

group by	orders.product_id, orders.main_category

order by	order_sum desc

limit 5