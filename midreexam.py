C-#insertone()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

uri = "mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'online_store' database
    db = client.online_store

    # Get reference to 'customers' collection
    customers_collection = db.customers

    # Inserting a new customer
    new_customer = {
        "customer_id": "CUST001",
        "name": "John Doe",
        "email": "john.doe@example.com",
        "address": "123 Main Street",
        "phone": "123-456-7890",
        "created_at": datetime.datetime.utcnow(),
    }
    result = customers_collection.insert_one(new_customer)
    customer_id = result.inserted_id
    print(f"Customer ID of inserted document: {customer_id}")

    # Get reference to 'product_reviews' collection
    product_reviews_collection = db.product_reviews

    # Inserting a new product review
    new_product_review = {
        "product_id": "PROD001",
        "customer_id": customer_id,
        "rating": 5,
        "comment": "Great product! Highly recommend.",
        "created_at": datetime.datetime.utcnow(),
    }
    result = product_reviews_collection.insert_one(new_product_review)
    review_id = result.inserted_id
    print(f"Review ID of inserted document: {review_id}")

    # Get reference to 'carts' collection
    carts_collection = db.carts

    # Inserting an item into a customer's cart
    new_cart_item = {
        "customer_id": customer_id,
        "product_id": "PROD002",
        "quantity": 2,
        "added_at": datetime.datetime.utcnow(),
    }
    result = carts_collection.insert_one(new_cart_item)
    cart_item_id = result.inserted_id
    print(f"Cart Item ID of inserted document: {cart_item_id}")

except Exception as e:
    print(e)
finally:
    client.close()




C-#Insert many()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

uri = "mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'online_store' database
    db = client.online_store

    # Get reference to 'customers' collection
    customers_collection = db.customers

    # Inserting many customers
    new_customers = [
        {
            "customer_id": "CUST001",
            "name": "Ada Lovelace",
            "email": "ada.lovelace@example.com",
            "address": "123 Main Street",
            "phone": "123-456-7890",
            "created_at": datetime.datetime.utcnow(),
        },
        {
            "customer_id": "CUST002",
            "name": "Muhammad ibn Musa al-Khwarizmi",
            "email": "al-khwarizmi@example.com",
            "address": "456 Oak Avenue",
            "phone": "987-654-3210",
            "created_at": datetime.datetime.utcnow(),
        },
    ]

    # Write an expression that inserts the 'new_customers' documents into the 'customers' collection.
    result = customers_collection.insert_many(new_customers)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

    # Get reference to 'product_reviews' collection
    product_reviews_collection = db.product_reviews

    # Inserting many product reviews
    new_product_reviews = [
        {
            "product_id": "PROD001",
            "customer_id": "CUST001",
            "rating": 5,
            "comment": "Great product! Highly recommend.",
            "created_at": datetime.datetime.utcnow(),
        },
        {
            "product_id": "PROD002",
            "customer_id": "CUST002",
            "rating": 4,
            "comment": "Good product, but could be improved.",
            "created_at": datetime.datetime.utcnow(),
        },
    ]

    # Write an expression that inserts the 'new_product_reviews' documents into the 'product_reviews' collection.
    result = product_reviews_collection.insert_many(new_product_reviews)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

    # Get reference to 'carts' collection
    carts_collection = db.carts

    # Inserting many items into customers' carts
    new_cart_items = [
        {
            "customer_id": "CUST001",
            "product_id": "PROD003",
            "quantity": 2,
            "added_at": datetime.datetime.utcnow(),
        },
        {
            "customer_id": "CUST002",
            "product_id": "PROD001",
            "quantity": 1,
            "added_at": datetime.datetime.utcnow(),
        },
    ]

    # Write an expression that inserts the 'new_cart_items' documents into the 'carts' collection.
    result = carts_collection.insert_many(new_cart_items)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

except Exception as e:
    print(e)
finally:
    client.close()

R-Find()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'online_store' database
    db = client.online_store

    # Get reference to 'customers' collection
    customers_collection = db.customers

    # Finding a customer by ID
    customer_id_to_find = "CUST001"
    query = {
        "customer_id": customer_id_to_find
    }
    customer = customers_collection.find_one(query)
    print(customer)

    if customer:
        pprint.pprint(customer)
    else:
        print(f"No customer found with ID: {customer_id_to_find}")

except Exception as e:
    print(e)
finally:
    client.close()


R-#findmany()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'online_store' database
    db = client.online_store

    # Get reference to 'products' collection
    products_collection = db.products

    # Finding products with price greater than 50
    query = {
        "price": {"$gt": 50}
    }
    cursor = products_collection.find(query)

    num_products = 0
    for product in cursor:
        num_products += 1
        pprint.pprint(product)
        print()
    print("# of products found: " + str(num_products))

except Exception as e:
    print(e)
finally:
    client.close()


U-Update one ()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'online_store' database
    db = client.online_store

    # Get reference to 'products' collection
    products_collection = db.products

    # Finding products with price greater than 50
    query = {
        "price": {"$gt": 50}
    }
    cursor = products_collection.find(query)

    num_products = 0
    for product in cursor:
        num_products += 1
        pprint.pprint(product)
        print()
    print("# of products found: " + str(num_products))

except Exception as e:
    print(e)
finally:
    client.close()


U-updatemany()
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'online_store' database
    db = client.online_store

    # Get reference to 'accounts' collection
    accounts_collection = db.accounts

    # Filter - Find accounts with type 'savings'
    query = {"account_type": "savings"}

    # Update - Set a minimum balance requirement for savings accounts
    update_operation = {"$set": {"minimum_balance": 100}}
    print(update_operation)
    # Print original document(s)
    original_documents = list(accounts_collection.find(query))
    print("Original documents:")
    pprint.pprint(original_documents)

    # Update documents
    result = accounts_collection.update_many(query, update_operation)
    print("Documents matched: " + str(result.matched_count))
    print("Documents updated: " + str(result.modified_count))

    # Print updated document(s)
    updated_documents = list(accounts_collection.find(query))
    print("Updated documents:")
    pprint.pprint(updated_documents)

except Exception as e:
    print(e)
finally:
    client.close()


D-deleteone()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'online_store' database
    db = client.online_store

    # Get reference to 'carts' collection
    carts_collection = db.carts

    # Define the filter to identify the item to delete
    query = {"customer_id": "CUST001", "product_id": "PROD001"}

    # Print the document to be deleted
    print("Document to be deleted:")
    pprint.pprint(carts_collection.find_one(query))

    # Perform the delete operation
    result = carts_collection.delete_one(query)
    print("Documents matched: " + str(result.deleted_count))

except Exception as e:
    print(e)
finally:
    client.close()


D-deletemany()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'online_store' database
    db = client.online_store

    # Get reference to 'carts' collection
    carts_collection = db.carts

    # Perform the delete all operation
    result = carts_collection.delete_many({})

    print("Documents matched: " + str(result.deleted_count))

except Exception as e:
    print(e)
finally:
    client.close()
