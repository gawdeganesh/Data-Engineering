import pandas as pd
import random
import faker

# Initialize a Faker generator
fake = faker.Faker()

# Number of records
n_records = 10000
unique_orders = 1000
unique_products = 100

# Function to generate fake customer data
def generate_customers(n):
    customers = {
        "customer_id": range(1, n + 1),
        "customer_name": [fake.name() for _ in range(n)],
        "customer_phone": [fake.phone_number() for _ in range(n)],
        "customer_email": [fake.email() for _ in range(n)],
        "other_customer_details": [fake.text(max_nb_chars=200) for _ in range(n)]
    }
    return pd.DataFrame(customers)

# Generate Suppliers data
def generate_suppliers(n):
    suppliers = {
        "supplier_id": range(1, n + 1),
        "supplier_name": [fake.company() for _ in range(n)],
        "other_supplier_details": [fake.text(max_nb_chars=200) for _ in range(n)]
    }
    return pd.DataFrame(suppliers)


# Generate Products data
def generate_products(n, suppliers_n):
    products = {
        "product_id": range(1, n + 1),
        "product_type_code": [random.randint(1, 100) for _ in range(n)],
        "supplier_id": [random.randint(1, suppliers_n) for _ in range(n)],
        "product_price": [random.uniform(0.99, 1000.0) for _ in range(n)],
        "other_product_details": [fake.text(max_nb_chars=200) for _ in range(n)]
    }
    return pd.DataFrame(products)

# Generate Address data
def generate_addresses(n):
    addresses = {
        "address_id": range(1, n + 1),
        "line_1_number_building": [fake.building_number() for _ in range(n)],
        "line_2_number_street": [fake.street_name() for _ in range(n)],
        "line_3_area_locality": [fake.city_suffix() for _ in range(n)],
        "city": [fake.city() for _ in range(n)],
        "zip_postcode": [fake.zipcode() for _ in range(n)],
        "state_province_county": [fake.state() for _ in range(n)],
        "iso_country_code": [fake.country_code() for _ in range(n)],
        "other_address_details": [fake.text(max_nb_chars=200) for _ in range(n)]
    }
    return pd.DataFrame(addresses)

# Generate Customer_Orders data
def generate_customer_orders(n, customers_n):
    customer_orders = {
        "order_id": range(1, n + 1),
        "customer_id": [random.randint(1, customers_n) for _ in range(n)],
        "customer_payment_method_id": [random.randint(1, 10) for _ in range(n)],
        "order_status_code": [random.randint(1, 5) for _ in range(n)],
        "date_order_placed": [fake.date_between(start_date='-2y', end_date='today') for _ in range(n)],
        "date_order_paid": [fake.date_between(start_date='-2y', end_date='today') for _ in range(n)],
        "order_price": [random.uniform(20.0, 5000.0) for _ in range(n)],
        "other_order_details": [fake.text(max_nb_chars=200) for _ in range(n)]
    }
    return pd.DataFrame(customer_orders)

# Generate Ref_Address_Types data
def generate_ref_address_types(n):
    ref_address_types = {
        "address_type_code": range(1, n + 1),
        "address_type_description": [fake.job() for _ in range(n)]  # Just for dummy descriptions
    }
    return pd.DataFrame(ref_address_types)

# Function to generate fake customer addresses data
def generate_customer_addresses(customers, n):
    customer_addresses = {
        "customer_id": random.choices(customers, k=n),
        "address_id": range(1, n + 1),
        "date_from": [fake.date_between(start_date='-5y', end_date='today') for _ in range(n)],
        "date_to": [fake.date_between(start_date='today', end_date='+5y') for _ in range(n)],
        "address_type_code": [random.randint(1, 5) for _ in range(n)]
    }
    return pd.DataFrame(customer_addresses)

# Function to generate fake customer orders products data
def generate_customer_orders_products(orders, products, n):
    customer_orders_products = {
        "order_id": random.choices(orders, k=n),
        "product_id": random.choices(products, k=n),
        "quantity": [random.randint(1, 10) for _ in range(n)],
        "comments": [fake.text(max_nb_chars=200) for _ in range(n)]
    }
    return pd.DataFrame(customer_orders_products)

# Function to generate fake customer orders delivery data
def generate_customer_orders_delivery(orders, n):
    customer_orders_delivery = {
        "order_id": random.sample(orders, k=n),
        "date_reported": [fake.date_between(start_date='-1y', end_date='today') for _ in range(n)],
        "delivery_status_code": [random.randint(1, 5) for _ in range(n)]
    }
    return pd.DataFrame(customer_orders_delivery)


customers_df = generate_customers(n_records)
suppliers_df = generate_suppliers(500)  # Generating fewer suppliers
products_df = generate_products(2000, 500)  # Generating fewer products, but enough for variety
addresses_df = generate_addresses(5000)  # Generating a reasonable number of addresses
ref_address_types_df = generate_ref_address_types(10)  # Generating a few address types
customer_orders_df = generate_customer_orders(n_records, n_records)  # Using the same number of customers
customer_addresses_df = generate_customer_addresses(customers_df['customer_id'].tolist(), n_records)
customer_orders_products_df = generate_customer_orders_products(range(1, unique_orders + 1), 
                                                               range(1, unique_products + 1), 
                                                               n_records)
customer_orders_delivery_df = generate_customer_orders_delivery(range(1, unique_orders + 1), unique_orders)

# Save the data to a CSV file
customers_csv_path = 'Pyspark Practice/data/customers_data.csv'
suppliers_csv_path = 'Pyspark Practice/data/suppliers_data.csv'
products_csv_path = 'Pyspark Practice/data/products_data.csv'
addresses_csv_path = 'Pyspark Practice/data/addresses_data.csv'
customer_orders_csv_path = 'Pyspark Practice/data/customer_orders_data.csv'
ref_address_types_csv_path = 'Pyspark Practice/data/ref_address_types_data.csv'
customer_addresses_csv_path = 'Pyspark Practice/data/customer_addresses_data.csv'
customer_orders_products_csv_path = 'Pyspark Practice/data/customer_orders_products_data.csv'
customer_orders_delivery_csv_path = 'Pyspark Practice/data/customer_orders_delivery_data.csv'

customers_df.to_csv(customers_csv_path, index=False)
suppliers_df.to_csv(suppliers_csv_path, index=False)
products_df.to_csv(products_csv_path, index=False)
addresses_df.to_csv(addresses_csv_path, index=False)
customer_orders_df.to_csv(customer_orders_csv_path, index=False)
ref_address_types_df.to_csv(ref_address_types_csv_path, index=False)
customer_addresses_df.to_csv(customer_addresses_csv_path, index=False)
customer_orders_products_df.to_csv(customer_orders_products_csv_path, index=False)
customer_orders_delivery_df.to_csv(customer_orders_delivery_csv_path, index=False)







