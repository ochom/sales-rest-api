from django.db import models
import uuid
import os


def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    uuidname = "{}.{}".format(uuid.uuid4(), extension)
    return os.path.join('images/products', uuidname)


class AgentModel(models.Model):
    username = models.CharField(default='', max_length=100, unique=True)
    name = models.CharField(default='', max_length=100)
    address = models.CharField(default='', max_length=100)
    email = models.EmailField(default='', max_length=255)
    password = models.TextField(default='')
    rating = models.IntegerField(default=1)


class AgentSkillModel(models.Model):
    agent_id = models.CharField(default='', max_length=100, unique=True)
    skill = models.CharField(default='', max_length=100)


class ClientModel(models.Model):
    username = models.CharField(default='', max_length=100, unique=True)
    name = models.CharField(default='', max_length=100)
    address = models.CharField(default='', max_length=100)
    email = models.EmailField(default='', max_length=255)
    password = models.TextField(default='')
    location = models.CharField(default='0,0', max_length=100)

    def _str_(self):
        return self.username


class OrderModel(models.Model):
    client_id = models.IntegerField(default=0)
    agent_id = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    total_cost = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='placed', max_length=50)  # placed, ontransit, delivered, rejected


class ProductModel(models.Model):
    product_name = models.CharField(default='', max_length=100, unique=True)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    image = models.FileField("Image upload", default='', upload_to=scramble_uploaded_filename, null=True, blank=True)
    units = models.TextField(default='')

