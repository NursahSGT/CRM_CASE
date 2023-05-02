-- Create the orders table
CREATE TABLE orders (
  order_id VARCHAR(10) PRIMARY KEY,
  customer_id VARCHAR(10),
  order_date TIMESTAMP,
  order_platform_id INT,
  order_platform_name VARCHAR(50),
  product_id INT,
  main_category VARCHAR(50),
  order_quantity INT,
  order_amount NUMERIC(10,2)
);

-- Create the customer table
CREATE TABLE customer (
  customer_id VARCHAR(10) PRIMARY KEY,
  membership_date TIMESTAMP,
  communication_permission INT,
  customer_age INT,
  order_amount_6 NUMERIC(10,2),
  order_amount_12 NUMERIC(10,2),
  order_amount_24 NUMERIC(10,2),
  order_amount_36 NUMERIC(10,2),
  order_amount_48 NUMERIC(10,2),
  basket_average_6 NUMERIC(10,2),
  basket_average_12 NUMERIC(10,2),
  basket_average_24 NUMERIC(10,2),
  basket_average_36 NUMERIC(10,2),
  basket_average_48 NUMERIC(10,2),
  frequency_6 NUMERIC(10,6),
  frequency_12 NUMERIC(10,6),
  frequency_24 NUMERIC(10,6),
  frequency_36 NUMERIC(10,6),
  frequency_48 NUMERIC(10,6)
);

-- Create the customer_category_24 table
CREATE TABLE customer_category_24 (
  customer_id VARCHAR(10) PRIMARY KEY,
  book_flag INT,
  e_book_flag INT,
  electronic_flag INT,
  stationery_flag INT,
  hobby_toys_flag INT,
  music_flag INT,
  sport_outdoor_flag INT,
  personal_products_flag INT,
  other_flag INT
);

-- Add foreign keys to orders and customer tables
ALTER TABLE orders ADD FOREIGN KEY (customer_id) REFERENCES customer(customer_id);
ALTER TABLE customer_category_24 ADD FOREIGN KEY (customer_id) REFERENCES customer(customer_id);
