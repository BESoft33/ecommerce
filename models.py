from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=50)
	color = models.CharField(max_length= 20)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural='Categories'


class Brand(models.Model):
	company = models.CharField(max_length= 50)
	category =models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.company


class Item(models.Model):
	model = models.CharField(max_length= 50)
	price = models.FloatField()
	description = models.TextField()
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

	def __str__(self):
		return self.model

class User(models.Model):
	fname = models.CharField(max_length=20)
	lname = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	contact = models.CharField(max_length=10)
	orders = models.ForeignKey(Item, on_delete=models.CASCADE,default=None, blank=True)

	def __str__(self):
		return (self.fname+ " "+self.lname)


