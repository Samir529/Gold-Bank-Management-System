from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# class User(models.Model):
#     user = models.CharField(max_length=30, default='0')
#     first_name = models.CharField(max_length=30, default='0')
#     last_name = models.CharField(max_length=30, default='0')
#     email = models.EmailField(default='0')
locations= [
    ('Dhaka', 'Dhaka'),
    ('Narayanganj', 'Narayanganj'),
    ('Gazipur', 'Gazipur'),
    ('Cumilla', 'Cumilla'),
    ('Chittagong', 'Chittagong'),
    ('Noakhali', 'Noakhali'),
    ('Jessore', 'Jessore'),
    ('Khulna', 'Khulna'),
    ('Barisal', 'Barisal'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Feni', 'Feni'),
    ('Pabna', 'Pabna'),
    ('Faridpur', 'Faridpur'),
    ('Dinajpur', 'Dinajpur'),
    ('Coxs Bazar', 'Coxs Bazar'),
    ('Bogra', 'Bogra'),
    ('Tangail', 'Tangail'),
    ('Patuakhali', 'Patuakhali'),
    ('Lalmonirhat', 'Lalmonirhat'),
    ('Madaripur', 'Madaripur'),
    ('Mars', 'Mars')
    ]

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    # username = models.CharField(max_length=30, default='')
    # first_name = models.CharField(max_length=30, default='')
    # last_name = models.CharField(max_length=30, default='')
    # email = models.EmailField(default='')
    dateofbirth = models.DateField(blank=True, null=True, default=timezone.now)
    # nid = models.IntegerField(default='0')
    currentdate = models.DateField(default=timezone.now)
    location = models.CharField(max_length=30, default='', blank=True, null=True, choices=locations)
    mobileNo = models.CharField(max_length=11, default='', blank=True, null=True)
    account_age = models.CharField(max_length=10, default='', blank=True, null=True)
    # acc_no = models.IntegerField(default='-', blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profiles_pic', default='/profiles_pic/demo_profile_pic2.png', blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)


class deposit(models.Model):
    username = models.CharField(max_length=30, default='0')
    password = models.CharField(max_length=30, default='0')
    email = models.EmailField(default='0')
    currentdate = models.DateField(default=timezone.now)
    withdrawdate = models.DateField(null=True, blank=True, default=timezone.now)
    balance = models.FloatField(max_length=30, default='0')
    initial_balance = models.FloatField(max_length=30, default='0')
    last_withdraw_amount = models.FloatField(max_length=30, default='0')
    balance_in_gold = models.FloatField(max_length=30, default='0')
    gold_price_at_creation = models.FloatField(max_length=30, default='0.0')
    interest_balance = models.FloatField(max_length=30, default='0')
    monthly_interest_balance = models.FloatField(max_length=30, default='0')
    trigger = models.CharField(max_length=30, default='0')
    objects = models.Manager()

    def __str__(self):
        return self.username

class deposit_history(models.Model):
    username = models.CharField(max_length=30, default='0')
    email = models.EmailField(default='0')
    currentdate = models.DateField(default=timezone.now)
    amount = models.FloatField(max_length=30, default='0')
    objects = models.Manager()

    def __str__(self):
        return self.username

class withdraw_history(models.Model):
    username = models.CharField(max_length=30, default='0')
    email = models.EmailField(default='0')
    currentdate = models.DateField(default=timezone.now)
    amount = models.FloatField(max_length=30, default='0')
    objects = models.Manager()

    def __str__(self):
        return self.username

class loan(models.Model):
    username = models.CharField(max_length=30, default='0')
    password = models.CharField(max_length=30, default='0')
    email = models.EmailField(default='0')
    currentdate = models.DateField(default=timezone.now)
    amount = models.FloatField(max_length=30, default='0')
    return_date = models.DateField(default=timezone.now, null=True, blank=True)
    return_amount = models.FloatField(max_length=30, default='0')
    bank_profit = models.FloatField(max_length=30, default='0')
    status = models.CharField(max_length=30, default='')
    objects = models.Manager()

    def __str__(self):
        return self.username


class priceOfGold(models.Model):
    serial = models.CharField(max_length=10, default='0', null=True)
    date = models.DateField(default=timezone.now, blank=False)
    gold_price = models.FloatField(max_length=30,default='0.0')
    objects = models.Manager()

    def __str__(self):
        return self.serial

class products(models.Model):
    username = models.CharField(max_length=30, default='0')
    password = models.CharField(max_length=30, default='0')
    currentdate = models.DateField(default=timezone.now)
    coin_type = models.CharField(max_length=10, default='-', blank=True, null=True)
    quantity = models.CharField(max_length=10, default='-', blank=True, null=True)
    price = models.FloatField(max_length=30, default='0')
    coin_picture = models.ImageField(upload_to='profiles_coin', blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.username

class bankMoney(models.Model):
    serial = models.CharField(max_length=10, default='0', null=True)
    amount = models.FloatField(max_length=100, default='0', null=True)
    objects = models.Manager()



