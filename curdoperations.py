from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint  # Added import for pprint

uri = "mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
    db = client.bank

    # Get reference to 'accounts' collection
    accounts_collection = db.accounts

    # Inserting one account
    new_account = {
        "account_holder": "Linus Torvalds",
        "account_id": "MDB829001337",
        "account_type": "checking",
        "balance": 50352434,
        "last_updated": datetime.datetime.utcnow(),
    }  # Added comment for clarity

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = accounts_collection.insert_one(new_account)

    document_id = result.inserted_id
    pprint(f"_id of inserted document: {document_id}")

except Exception as e:
    print(e)
finally:
    client.close()




from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

uri =" mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'social_media' database (use your preferred database name)
    db = client.social_media

    # Get reference to 'users' collection (representing Instagram-like accounts)
    users_collection = db.users

    # Inserting many Instagram-like accounts
    new_accounts = [
        {
            "username": "adalovely",
            "full_name": "Ada Lovelace",
            "email": "ada@example.com",
            "followers": 500,
            "posts": [
                {"content": "Hello World!", "timestamp": datetime.datetime.utcnow()},
                {"content": "Coding in Python!", "timestamp": datetime.datetime.utcnow()},
            ]
        },
        {
            "username": "muhammadmath",
            "full_name": "Muhammad al-Khwarizmi",
            "email": "muhammad@example.com",
            "followers": 1000,
            "posts": [
                {"content": "Algorithms are fascinating!", "timestamp": datetime.datetime.utcnow()},
                {"content": "Mathematics is the key!", "timestamp": datetime.datetime.utcnow()},
            ]
        },
    ]

    # Write an expression that inserts the 'new_accounts' documents into the 'users' collection.
    result = users_collection.insert_many(new_accounts)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

except Exception as e:
    print(e)
finally:
    client.close()





from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint
import datetime

uri = "mongodb+srv://jyothithumma28:honeyreddy@cluster0.m1y2gpz.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'social_media' database (use your preferred database name)
    db = client.social_media

    # Get reference to 'users' collection (representing Instagram-like accounts)
    users_collection = db.users

    # Find users with more than 1000 followers
    query = {"followers": {"$gt": 1000}}

    # Write an expression that selects the documents matching the query constraint in the 'users' collection.
    cursor = users_collection.find(query)

    num_docs = 0
    for document in cursor:
        num_docs += 1
        pprint.pprint(document)
        print()
    print("# of documents found: " + str(num_docs))

except Exception as e:
    print(e)
finally:
    client.close()



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

    # Get reference to 'social_media' database (use your preferred database name)
    db = client.social_media

    # Get reference to 'users' collection (representing Instagram-like accounts)
    users_collection = db.users

    # Find an Instagram-like account by _id
    document_to_find = {
        "_id": ObjectId("65c2caeaae6140696995984e")
    }

    # Write an expression that finds the document in the 'users' collection.
    result = users_collection.find_one(document_to_find)

    pprint.pprint(result)

except Exception as e:
    print(e)
finally:
    client.close()



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

    # Get reference to 'social_media' database (use your preferred database name)
    db = client.social_media

    # Get reference to 'users' collection (representing Instagram-like accounts)
    users_collection = db.users

    # Filter: Find the user you want to update
    user_to_update = {"_id": ObjectId("65c2cb3a004800a420ffc3dd")}

    # Update: Increment the followers count by 100
    update_followers = {"$inc": {"followers": 100}}

    # Print original user document
    pprint.pprint(users_collection.find_one(user_to_update))

    # Write an expression that updates the target user's followers count by the specified amount.
    result = users_collection.update_one(user_to_update, update_followers)
    print("Documents updated: " + str(result.modified_count))

    # Print updated user document
    pprint.pprint(users_collection.find_one(user_to_update))

except Exception as e:
    print(e)
finally:
    client.close()



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

    # Get reference to 'social_media' database (use your preferred database name)
    db = client.social_media

    # Get reference to 'users' collection (representing Instagram-like accounts)
    users_collection = db.users

    # Filter: Find users with a follower count above a certain threshold
    filter_condition = {"followers": {"$gt": 1000}}

    # Print original user documents
    pprint.pprint(list(users_collection.find(filter_condition)))

    # Update: Set the account type to "premium" for selected users
    update_account_type = {"$set": {"account_type": "premium"}}

    # Write an expression that updates the account type for users based on the filter condition.
    result = users_collection.update_many(filter_condition, update_account_type)
    print("Documents matched: " + str(result.matched_count))
    print("Documents updated: " + str(result.modified_count))

    # Print updated user documents
    pprint.pprint(list(users_collection.find(filter_condition)))

except Exception as e:
    print(e)
finally:
    client.close()     




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

    # Get reference to 'social_media' database (use your preferred database name)
    db = client.social_media

    # Get reference to 'users' collection (representing Instagram-like accounts)
    users_collection = db.users

    # Filter: Find the user to delete by username
    filter_condition = {"username": "target_user"}

    # Search for the user document before delete
    print("Searching for target user before delete: ")
    pprint.pprint(users_collection.find_one(filter_condition))

    # Write an expression that deletes the target user.
    result = users_collection.delete_one(filter_condition)

    # Search for the user document after delete
    print("Searching for target user after delete: ")
    pprint.pprint(users_collection.find_one(filter_condition))

    print("Documents deleted: " + str(result.deleted_count))

except Exception as e:
    print(e)
finally:
    client.close()  



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

    # Get reference to 'social_media' database (use your preferred database name)
    db = client.social_media

    # Get reference to 'users' collection (representing Instagram-like accounts)
    users_collection = db.users

    # Filter: Find users with fewer than 100 followers
    filter_condition = {"followers": {"$lt": 100}}

    # Search for sample user documents before delete
    print("Searching for sample target users before delete: ")
    pprint.pprint(list(users_collection.find(filter_condition)))

    # Write an expression that deletes the target users.
    result = users_collection.delete_many(filter_condition)

    # Search for sample user documents after delete
    print("Searching for sample target users after delete: ")
    pprint.pprint(list(users_collection.find(filter_condition)))

    print("Documents deleted: " + str(result.deleted_count))

except Exception as e:
    print(e)
finally:
    client.close()






