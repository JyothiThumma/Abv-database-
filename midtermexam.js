//section 3:
{
  "_id": ObjectId("60900a3f0fd9ff01c86c7a7a"),
  "username": "swathi_marri",
  "name": "swathi marri",
  "age": 35,
  "email": "swathi@marri.com",
  "purchases": [
    {
      "product": "Pixel",
      "price": 599.99
    },
    {
      "product": "windows",
      "price": 1299.99
    }
  ]
}
//section3:
CREATE TABLE Users (
  user_id INT PRIMARY KEY,
  username VARCHAR(50),
  name VARCHAR(100),
  age INT,
  email VARCHAR(100)
);
CREATE TABLE Purchases (
  purchase_id INT PRIMARY KEY,
  user_id INT,
  product VARCHAR(100),
  price DECIMAL(10, 2),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
//section4:
// Collection: Products
{
  "_id": ObjectId("60900a3f0fd9ff01c86c7a7a"),
  "name": "Laptop",
  "price": 999.99,
  "description": "High-performance laptop",
  "category": "Electronics"
}
//section10:
# Import the MongoClient class from the pymongo package
from pymongo import MongoClient

# Connect to the MongoDB server running on localhost
client = MongoClient('localhost', 27017)

# Access or create a database named 'mydatabase'
db = client['mydatabase']

# Access or create a collection named 'mycollection' within the 'mydatabase' database
collection = db['mycollection']

# 1. Create (Insert) Operation
# Insert a single document into the collection
document1 = {"name": "Alice", "age": 30, "city": "New York"}
result = collection.insert_one(document1)
print("Inserted document id:", result.inserted_id)

# 2. Read Operation
# Find a document by a specific field value
result = collection.find_one({"name": "Alice"})
print("Found document:", result)

# 3. Update Operation
# Update a document by specifying a filter and the new data
update_filter = {"name": "Alice"}
new_data = {"$set": {"age": 31}}  # Update Alice's age
result = collection.update_one(update_filter, new_data)
print("Updated", result.modified_count, "document")

# 4. Delete Operation
# Delete a document by specifying a filter
delete_filter = {"name": "Alice"}
result = collection.delete_one(delete_filter)
print("Deleted", result.deleted_count, "document")
//section6
from django.db import models

# Connect to database
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "mydatabase",
    }
}

# Define a Django model
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

# Access data using Django ORM
users = User.objects.all()
for user in users:
    print(user.name, user.email)
//section6:
from mongoengine import connect, Document

# Connect to database
connect("mydatabase")

# Define a document model
class User(Document):
    name = StringField()
    email = EmailField()

# Create and save a document
user = User(name="John Doe", email="johndoe@example.com")
user.save()

# Find documents
users = User.objects.all()
for user in users:
    print(user.name, user.email)
//section7:
# Find all documents
documents = collection.find()

# Find documents with specific criteria
for document in collection.find({"age": {"$gt": 25}}):
    print(document)
# Insert single document
collection.insert_one({"name": "Priyanka", "age": 30})

# Insert multiple documents
documents = [{"name": "Priya", "age": 25}, {"name": "Parisa", "age": 40}]
collection.insert_many(documents)

//section8:
Import MongoClient class from pymongo package
from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient()

# Access the desired database
db = client.mydatabase

# Access the desired collection
collection = db.mycollection

# Define the filter to identify documents to delete
filter = {"age": {"$gte": 40}}  # Delete documents with age greater than or equal to 40

# Delete a single document matching the filter
result = collection.deleteOne(filter)

# Print the number of documents deleted
print("Number of documents deleted:", result.deleted_count)
//section8:
# Import MongoClient class from pymongo package
from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient()

# Access the desired database
db = client.mydatabase

# Access the desired collection
collection = db.mycollection

# Define the filter to identify the document to replace
filter = {"name": "Priya"}

# Define the new document with updated fields
new_document = {
    "name": "Priya",
    "age": 35,
    "city": "HArtford"
}

# Replace the existing document with the new one
result = collection.replaceOne(filter, new_document)

# Print the number of documents replaced
print("Number of documents replaced:", result.modified_count)




