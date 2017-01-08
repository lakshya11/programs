from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Players(models.Model):
	name = models.CharField(max_length=200)
	username = models.CharField(max_length=200)

class Winners(models.Model):
	player = models.ForeignKey(Players, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)
	position = models.CharField(max_length=200)

class Ticket(models.Model):
	ticket_number = models.CharField(max_length=200) # unique random number
	x1 = models.IntegerField()
	x2 = models.IntegerField()
	x3 = models.IntegerField()
	x4 = models.IntegerField()
	x5 = models.IntegerField()
	x6 = models.IntegerField()
	x7 = models.IntegerField()
	x8 = models.IntegerField()
	x9 = models.IntegerField()
	y1 = models.IntegerField()
	y2 = models.IntegerField()
	y3 = models.IntegerField()
	y4 = models.IntegerField()
	y5 = models.IntegerField()
	y6 = models.IntegerField()
	y7 = models.IntegerField()
	y8 = models.IntegerField()
	y9 = models.IntegerField()
	z1 = models.IntegerField()
	z2 = models.IntegerField()
	z3 = models.IntegerField()
	z4 = models.IntegerField()
	z5 = models.IntegerField()
	z6 = models.IntegerField()
	z7 = models.IntegerField()
	z8 = models.IntegerField()
	z9 = models.IntegerField()

class TokensGenerated(models.Model):
	token = models.IntegerField()
	time = models.DateTimeField(auto_now=True)

class TicketsGenerated(models.Model):
	player = models.ForeignKey(Players, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

class TicketsStatus(models.Model):
	player = models.ForeignKey(Players,on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)
	ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
	










