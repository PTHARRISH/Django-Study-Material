# Serializers
# https://www.django-rest-framework.org/api-guide/serializers/

# Serializers allow complex data such as querysets
# and model instances to be converted to native Python datatypes
# that can then be easily rendered into JSON, XML or other content types.
# Serializers also provide deserialization,
# allowing parsed data to be converted back into complex types,
# after first validating the incoming data.

# The serializers in REST framework work very similarly to Django's Form
# and ModelForm classes.
# We provide a Serializer class which gives you a powerful,
# generic way to control the output of your responses,
# as well as a ModelSerializer class which provides a useful shortcut
# for creating serializers that deal with model instances and querysets.


# Serializer fields handle converting between primitive values
# and internal datatypes.
# They also deal with validating input values,
# as well as retrieving and setting the values from their parent objects.



# Field-level validation
# You can specify custom field-level validation by adding .
# validate_<field_name> methods to your Serializer subclass. 
# These are similar to the .clean_<field_name> methods on Django forms.



# Serializer Fields:

# Core arguments
# read_only:
# Read-only fields are included in the API output,
# but should not be included in the input during create or update operations.
# Any 'read_only' fields that are incorrectly included in the serializer
# input will be ignored.
# Set this to True to ensure that the field is used when serializing a representation,
# but is not used when creating or updating an instance during deserialization.
# Defaults to False

# The read_only=True parameter creates a one-way valve in your API:

# The read_only parameter is one of the most commonly used
# serializer field arguments in Django REST Framework.
# Here are practical, real-world examples demonstrating when and how to use it:
# In this example:

# id: Primary keys should never be editable by users during creation/updates

# date_joined: Automatically set when the user is created, shouldn't be modified

# last_login: System-managed field that tracks authentication, not user input


# write_only:
# Set this to True to ensure that the field may be used
# when updating or creating an instance,
# but is not included when serializing the representation.

# Defaults to False

# Password Fields:
# The most common use case for write_only=True is password fields.
# You want users to be able to set or update passwords,
# but you never want to include the password in API responses for security reasons


# def validate_price(self,value):
# When Validation Methods Are Called

# Validation methods like validate_price() are executed only during:
# Deserialization (incoming data → Python objects)
# When serializer.is_valid() is called
# During CREATE or UPDATE operations


# Nested Serializer
# The code items=OrderItemSerializer(many=True, read_only=True) 
# OrderItem model inside field we need to configure related_name='items' 
# then only it will display in Browsable API
# demonstrates the use of a nested serializer in Django REST Framework (DRF), 
# which is a powerful pattern for handling related data in API responses.

# This line defines a field in a serializer (likely an OrderSerializer) that:
# OrderItemSerializer: Uses another serializer to handle the nested items data
# many=True: Indicates this field contains multiple items (a list/array)
# read_only=True: Makes this field output-only - 
# it appears in API responses but cannot be modified through this serializer

# Instead of just basic order info:

# {
#     "id": 123,
#     "order_date": "2025-08-22",
#     "customer": "John Doe",
#     "total_amount": 299.99,
#     "status": "shipped"
# }

# You get complete order details with all items in one API call:

# {
#     "id": 123,
#     "order_date": "2025-08-22",
#     "customer": "John Doe",
#     "total_amount": 299.99,
#     "status": "shipped",
#     "items": [
#         {
#             "id": 456,
#             "product_name": "Wireless Headphones",
#             "quantity": 1,
#             "price": 199.99,
#             "subtotal": 199.99
#         },
#         {
#             "id": 457,
#             "product_name": "Phone Case",
#             "quantity": 2,
#             "price": 50.00,
#             "subtotal": 100.00
#         }
#     ]
# }

# Without nested serializers, you'd face these challenges:

# Flat data structure: 
# API responses would only show order-level information

# Multiple API calls: 
# Frontend would need separate requests to get order details and item details

# Data inconsistency: 
# Risk of mismatched data between related models

# Poor user experience: 
# Slower loading times due to multiple network requests

# Benefits in Real-World Applications
# Performance: Reduces database queries and network requests 
# by fetching related data in one go

# Frontend Development: 
# Simplifies client-side code - 
# no need to manage multiple API calls and data merging

# Data Consistency: 
# Ensures all related data is from the same transaction/moment in time

# User Experience: 
# Faster page loads and fewer loading states for users

# API Design: 
# Creates more intuitive and RESTful endpoints 
# that match how users think about the data


# Serializer Field

# Creates a custom field called total_price in your serializer
# Uses SerializerMethodField - 
# a special DRF field type that gets its value from a custom method

# method_name="total" tells DRF to call the method named total() 
# to get the value for this field

# This field will appear in your API response as 
# "total_price": <calculated_value>

# python
# def total(self, obj): else def get_total_price(self, obj)

# What this line does:
# Defines the custom method that calculates the total_price value
# self refers to the serializer instance
# obj is the model instance being serialized (like an Order object)
# This method must return the value you want for the total_price field



# product = ProductSerializer() 
# without this it will display id but once you pass the product serializer 
# it will get the id relevent information will display
# Overrides the default product field behavior
# Without this line: 
# The API would only show the product ID (like "product": 5)

# With this line: 
# The API shows the complete product information using ProductSerializer
