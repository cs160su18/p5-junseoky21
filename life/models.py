from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)

class Customer(models.Model):
	name = models.CharField(max_length=64)

class Restaurant(models.Model):
	name = models.CharField(max_length=64)
	latitude = models.FloatField()
	longitude = models.FloatField()
	# rating = models.FloatField()
	# joined = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
	title = models.CharField(max_length=64)
	content = models.CharField(max_length=4096)
	rating = models.FloatField()
	datetime = models.DateTimeField(auto_now_add=True)
	verified = models.BooleanField()
	customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
	restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)

class LocationLogs(models.Model):
	datetime = models.DateTimeField(auto_now_add=True)
	latitude = models.FloatField()
	longitude = models.FloatField()


