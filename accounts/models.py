from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE

#django amader ke bulit in user make korar facility de
class UserBankAccount(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='account')
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE)
    account_num = models.IntegerField(unique=True) #account num duijon user er kokhono same hove nah coz unique true kore diyechi
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    #max_digits mean ekjon user 12 digit obdi taka rakte parbe
    #decimal_places mean ekjon user dosmik er por 2 digit dite parbe
    def __str__(self):
        return str(self.account_num)
    
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address') 
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.email)
