from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Cookie:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.order_qty = data['order_qty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def all(cls):
        query = "SELECT * FROM orders; "
        results = connectToMySQL('cookies_schema').query_db(query)
        cookies = []
        for i in results:
            cookies.append( cls(i) )
        return cookies
        
    @classmethod
    def order_info(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        results = connectToMySQL('cookies_schema').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query = "UPDATE orders SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, order_qty = %(order_qty)s, updated_at = NOW() WHERE id = %(id)s; "
        results = connectToMySQL('cookies_schema').query_db(query,data)
        return results

    @classmethod
    def add(cls, data):
        query = "INSERT INTO orders(customer_name, cookie_type, order_qty, created_at, updated_at) VALUES (%(customer_name)s, %(cookie_type)s,%(order_qty)s,NOW(), NOW()); "
        results = connectToMySQL('cookies_schema').query_db(query,data)
        return results

    @staticmethod
    def validate_add(cookies):
        is_valid = True 
        if len(cookies['customer_name']) <= 0:
            flash("**Customer Name is required.**", 'customer_name')
            is_valid = False
        if len(cookies['cookie_type']) <= 0:
            flash("**Cookie Type is required.**", 'cookie_type')
            is_valid = False
        if len(cookies['order_qty']) <= 0:
            flash("**Order Quantity is required.**", "order_qty")
            is_valid = False
        return is_valid