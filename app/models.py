import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """

    # You can add additional fields here if needed
    pass


# @property
# Computed Properties:
# Your in_stock property is a perfect example of a computed attribute.
# It dynamically calculates whether items are available
# based on the current stocks value, ensuring the result is always current.

# Clean Interface:
# The property decorator makes your model's interface more intuitive.
# Users can access in_stock as if it's a regular attribute,
# making the code more readable and Pythonic.

# Encapsulation:
# Properties provide a way to control access to data
# while maintaining a simple interface. You can add validation,
# logging, or other logic behind the scenes without changing
# how the property is accessed.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stocks = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    @property
    def in_stock(self):
        return self.stocks > 0

    def __str__(self):
        return self.name


# PositiveIntegerField
# The PositiveIntegerField is a Django model field designed
# to store non-negative integer values (including zero).
# It functions like a regular IntegerField
# but with built-in validation to ensure
# only positive numbers or zero are accepted.


# UUID
# Unique Identifiers:
# UUIDs provide globally unique identifiers
# that don't reveal information about your database size or
# record creation order, making them ideal for public-facing APIs.

# Security Enhancement:
# Unlike sequential integer IDs, UUIDs are unpredictable,
# preventing users from guessing other record IDs in your system.


class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "Pending"
        DELIVERED = "Delivered"
        CANCELED = "Canceled"

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING
    )
    products = models.ManyToManyField(
        Product, through="OrderItem", related_name="orders"
    )

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"


# ForeignKey:
# The ForeignKey with CASCADE creates a many-to-one relationship
# between models where deleting the referenced (parent) object
# automatically deletes all related (child) objects.

# Alternative Behaviors
# If you don't want orders deleted when users are deleted,
# you could use:

# PROTECT: Prevents User deletion if they have orders

# SET_NULL: Sets the user field to NULL (requires null=True)

# SET_DEFAULT: Sets a default user value

# Alternative - keeps orders when user is deleted
# user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# Important consideration:
# For e-commerce applications,
# you might want to preserve order history even
# after user accounts are deleted.
# In such cases, SET_NULL or PROTECT would be more appropriate than CASCADE


# Through
# The through parameter in ManyToManyField is used to add extra information
# to the many-to-many relationship by creating a custom intermediary model
# instead of Django's default join table.

# Why Use through?
# Without through, Django automatically creates a simple join table
# with only the foreign keys of the two related models. However,
# in e-commerce scenarios like your Order-Product relationship,
# you need to store additional information about the relationship itself.

# In your case, you likely need to store:

# Quantity of each product in the order

# Price at the time of purchase

# Discounts applied

# Product variations (size, color, etc.)

# Benefits in E-commerce
# Price History:
# Store the price at the time of purchase,
# even if product prices change later.

# Quantity Management:
# Track how many units of each product were ordered.

# Flexible Data:
# Add any additional fields needed for business logic
# (discounts, variations, notes).


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} X {self.product.name} in Order {self.order.order_id}"
