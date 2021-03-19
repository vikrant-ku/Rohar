from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=20, default="")
    subject = models.CharField(max_length=30, default="")
    message = models.TextField(default="")
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class Website_Budget(models.Model):
    responsive = models.CharField(max_length=15, default="")
    template = models.CharField(max_length=5, default="")
    type = models.CharField(max_length= 15, default="")
    design = models.CharField(max_length=20, default="")
    pages = models.CharField(max_length=5, default="")
    technologies = models.CharField(max_length=10, default="")
    name = models.CharField(max_length=30, default="")
    contact = models.CharField(max_length=30, default="")
    email = models.EmailField(default="")
    message = models.TextField(default="")
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Mobile_Budget(models.Model):
    responsive = models.CharField(max_length=15, default="")
    template = models.CharField(max_length=5, default="")
    type = models.CharField(max_length=15, default="")
    design = models.CharField(max_length=20, default="")
    pages = models.CharField(max_length=5, default="")
    database = models.CharField(max_length=5, default="")
    api = models.CharField(max_length=5, default="")
    name = models.CharField(max_length=30, default="")
    contact = models.CharField(max_length=30, default="")
    email = models.EmailField(default="")
    message = models.TextField(default="")
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class Web_Mobile_Budget(models.Model):
    responsive = models.CharField(max_length=15, default="")
    template = models.CharField(max_length=5, default="")
    technologies = models.CharField(max_length=20, default="")
    type = models.CharField(max_length=15, default="")
    design = models.CharField(max_length=20, default="")
    pages = models.CharField(max_length=5, default="")
    apptype = models.CharField(max_length=15, default="")
    name = models.CharField(max_length=30, default="")
    contact = models.CharField(max_length=30, default="")
    email = models.EmailField(default="")
    message = models.TextField(default="")
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

CATEGORY_CHOICES = (
        ('Fashion', 'Fashion' ),
        ('Product', 'Product'),
        )
class Photography(models.Model):
    title = models.CharField(max_length=30, default="")
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, null=True, blank=True)
    show = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title
