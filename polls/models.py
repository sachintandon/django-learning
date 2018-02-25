from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator
from fernet_fields import EncryptedTextField


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class UserAccount(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False )
    password = EncryptedTextField(models.CharField(max_length=40))
    mob_number = models.IntegerField(
        default=0000000000,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(10)
        ]
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)


class Account(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    Amount = models.DecimalField(null=False,blank=False , max_digits=20 ,decimal_places=2)
    OrderID = models.IntegerField(null=False,blank=False)
    VendorName = models.CharField(null=False,blank=False , max_length=500)
    Details = models.CharField(null=False , max_length=1000)
