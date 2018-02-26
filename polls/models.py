import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator,MaxLengthValidator,validate_email,MinValueValidator,MaxValueValidator
from fernet_fields import EncryptedTextField


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class UserAccount(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False, validators = [validate_email])
    password = EncryptedTextField(models.CharField(max_length=40,
                                                   verbose_name="Password")
                                  )
    mob_number = models.IntegerField(
        default=0000000000,
        validators=[
            MinValueValidator(1000000000),
            MaxValueValidator(9999999999)
        ]
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return 'User Account For %s with mobile number %s and email id as %s is created' % ( self.first_name ,self.mob_number , self.email)


class Account(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)
    Amount = models.DecimalField(null=False,blank=False , max_digits=20 ,decimal_places=2)
    OrderID = models.IntegerField(null=False,blank=False)
    VendorName = models.CharField(null=False,blank=False , max_length=500)
    Details = models.CharField(null=False , max_length=1000)
    def __str__(self):
        return self.OrderID,self.Amount
