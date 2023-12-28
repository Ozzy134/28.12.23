from django.contrib.auth.models import User
from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateField()
    is_published = models.BooleanField()
    category = models.ManyToManyField('Categories')
    comment = models.ManyToManyField('Comments')
    like = models.ForeignKey('Likes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Categories(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Comments(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment} написал {self.user.username}'

class Likes(models.Model):
    like = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Image(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField()

    def __str__(self):
        return self.title






# SFGSFGSFGSFGSFGSFBSCVCZSGF






class Prod(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Category(models.Model):
    name_cat = models.CharField(max_length=30)

    def __str__(self):
        return self.name_cat

class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    text = models.CharField(max_length=50)
    description = models.TextField()
    prodmen = models.ForeignKey(Prod, on_delete=models.CASCADE)
    images = models.ImageField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Zakaz(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    full_price = models.IntegerField()
    name_cliente = models.CharField(max_length=25)
    phone_cliente = models.CharField(max_length=11)

    def __str__(self):
        return self.product