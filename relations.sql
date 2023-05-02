ALTER TABLE orders ADD FOREIGN KEY (customer_id) REFERENCES customer(customer_id);
ALTER TABLE customer_category_24 ADD FOREIGN KEY (customer_id) REFERENCES customer(customer_id);