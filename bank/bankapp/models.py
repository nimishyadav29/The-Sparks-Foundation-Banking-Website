from django.db import models

# Create your models here.
class customer(models.Model):
    id=models.IntegerField(default=0,primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    accbal = models.IntegerField()
    accno = models.IntegerField()



class transfer_history(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True,null=True)
    sender =  models.CharField(max_length=255)
    senderaccno=models.IntegerField(default=0)
    receiveraccno = models.IntegerField(default=0)

    receiver =  models.CharField(max_length=255)
    amount = models.FloatField()