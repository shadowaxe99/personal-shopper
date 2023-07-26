```python
import json

# Importing the product data schema
from .data_schemas import ProductSchema

# Variable to store product data
productData = []

# Function to load product data
def load_product_data():
    global productData
    with open('product_data.json', 'r') as file:
        productData = json.load(file)

# Function to search for a product
def search_product(query):
    load_product_data()
    results = [product for product in productData if query.lower() in product['name'].lower()]
    return results

# Function to compare products
def compare_products(product_ids):
    load_product_data()
    products_to_compare = [product for product in productData if product['id'] in product_ids]
    comparison_data = {}
    for product in products_to_compare:
        comparison_data[product['id']] = {
            'name': product['name'],
            'price': product['price'],
            'features': product['features']
        }
    return comparison_data
```