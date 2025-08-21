# Serializers
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


# https://www.django-rest-framework.org/api-guide/serializers/