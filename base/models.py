from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True,  default='https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png')
    
    description = models.TextField(null=True, blank=True)
   
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)

    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):

    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address)
    
class New(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True, default='https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png')
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)
    
class Advert(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True, default='https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png')
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)
    
class Team(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    logo = models.CharField(max_length=200, null=True, blank=True, default='https://storage.googleapis.com/proudcity/mebanenc/uploads/2021/03/placeholder-image.png')
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.name)
    
class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team2')
    team1_score = models.IntegerField(null=True, blank=True, default=0)
    team2_score = models.IntegerField(null=True, blank=True, default=0)
    date = models.DateField(auto_now_add=False, null=True, blank=True)
    time = models.TimeField(auto_now_add=False, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    stadium = models.CharField(max_length=200, null=True, blank=True, default='St Sebastian Park')
    _id = models.AutoField(primary_key=True, editable=False)
    
    def day(self):
        return self.date.strftime('%d')
    
    
    def __str__(self):
        return str(self.team1) + ' vs ' + str(self.team2)
    
class Fixture(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team1_fixture')
    team2 = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team2_fixture')
    date = models.DateField(auto_now_add=False, null=True, blank=True)
    time = models.TimeField(auto_now_add=False, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    stadium = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.team1) + ' vs ' + str(self.team2)
    
    
class Table(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='team_table')
    played = models.IntegerField(null=True, blank=True, default=0)
    won = models.IntegerField(null=True, blank=True, default=0)
    drawn = models.IntegerField(null=True, blank=True, default=0)
    lost = models.IntegerField(null=True, blank=True, default=0)
    goals_for = models.IntegerField(null=True, blank=True, default=0)
    goals_against = models.IntegerField(null=True, blank=True, default=0)
    goal_difference = models.IntegerField(null=True, blank=True, default=0)
    points = models.IntegerField(null=True, blank=True, default=0)
    _id = models.AutoField(primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.team)