import psycopg2
import pandas as pd

host = "localhost"
port = 5432
database = "Turkuvaz"
user = "postgres"
password = "0211"

def create_connection():
    conn = None
    try:
        conn = psycopg2.connect(
                host=host,
                port=port,
                database=database,
                user=user,
                password=password)
        print("database successfully connected")
    except Exception as e:
        print("error", e)
    return conn

def get_target():
    db = None
    data = pd.DataFrame()
    try:
        db = create_connection()
        cursor = db.cursor()
        query = """
            SELECT	customer_age,
                    order_amount_6,
                    basket_average_6,
                    frequency_6,
                    customer_order_3_diff_month,
                    customer_only_electronic_3,
                    customer_first_only_book_later_diff_3,
                    customer_basket_median_greater_3,
                    target
                    
            FROM	target;
        """
        cursor.execute(query)
        data_from_sql = cursor.fetchall()
        if (data_from_sql):
            data = pd.DataFrame(
                data=data_from_sql,
                columns=[
                    "customer_age"
                    ,"order_amount_6"
                    ,"basket_average_6"
                    ,"frequency_6"
                    ,"customer_order_3_diff_month"
                    ,"customer_only_electronic_3"
                    ,"customer_first_only_book_later_diff_3"
                    ,"customer_basket_median_greater_3"
                    ,"target"
                ]
            )
    except Exception as e:
        print("error", e)
    finally:
        if db is not None:
            db.close()
    return data

def get_ml2():
    db = None
    data = pd.DataFrame()
    try:
        db = create_connection()
        cursor = db.cursor()
        query = """
            SELECT	customer_id,
                    TotalSales,
                    OrderCount,
                    AvgOrderValue
                    
            FROM	ml2;
        """
        cursor.execute(query)
        data_from_sql = cursor.fetchall()
        if (data_from_sql):
            data = pd.DataFrame(
                data=data_from_sql,
                columns=[
                    "customer_id",
                    "TotalSales",
                    "OrderCount",
                    "AvgOrderValue"
                ]
            )
    except Exception as e:
        print("error", e)
    finally:
        if db is not None:
            db.close()
    return data

def get_orders():
    db = None
    data = pd.DataFrame()
    try:
        db = create_connection()
        cursor = db.cursor()
        query = """
            SELECT  orders.order_id,
                    orders.customer_id,
                    orders.order_date,
                    orders.order_platform_id,
                    orders.order_platform_name,
                    orders.product_id,
                    orders.main_category,
                    orders.order_quantity,
                    orders.order_amount
            FROM orders;
        """
        cursor.execute(query)
        data_from_sql = cursor.fetchall()
        if (data_from_sql):
            data = pd.DataFrame(
                data=data_from_sql,
                columns=[
                    "order_id",
                    "customer_id",
                    "order_date",
                    "order_platform_id",
                    "order_platform_name",
                    "product_id",
                    "main_category",
                    "order_quantity",
                    "order_amount"
                ]
            )
    except Exception as e:
        print("error", e)
    finally:
        if db is not None:
            db.close()
    return data


def get_ml3():
    db = None
    data = pd.DataFrame()
    try:
        db = create_connection()
        cursor = db.cursor()
        query = """
            SELECT	customer_id,
                    TotalSales,
                    OrderCount,
                    AvgOrderValue,
                    Target
                    
            FROM	ml3;
        """
        cursor.execute(query)
        data_from_sql = cursor.fetchall()
        if (data_from_sql):
            data = pd.DataFrame(
                data=data_from_sql,
                columns=[
                    "customer_id",
                    "TotalSales",
                    "OrderCount",
                    "AvgOrderValue",
                    "Target"
                ]
            )
    except Exception as e:
        print("error", e)
    finally:
        if db is not None:
            db.close()
    return data

def get_cor():
    db = None
    data = pd.DataFrame()
    try:
        db = create_connection()
        cursor = db.cursor()
        query = """
            SELECT	"Spor & Outdoor",
                    "Hobi & Oyuncak",
                    "Diğer",
                    "E-Kitap",
                    "Müzik",
                    "Elektronik",
                    "Kırtasiye",
                    "Kişisel Ürünler"
                    
            FROM	cor;
        """
        cursor.execute(query)
        data_from_sql = cursor.fetchall()
        if (data_from_sql):
            data = pd.DataFrame(
                data=data_from_sql,
                columns=[
                    "Spor & Outdoor",
                    "Hobi & Oyuncak",
                    "Diğer",
                    "E-Kitap",
                    "Müzik",
                    "Elektronik",
                    "Kırtasiye",
                    "Kişisel Ürünler"
                ]
            )
    except Exception as e:
        print("error", e)
    finally:
        if db is not None:
            db.close()
    return data
