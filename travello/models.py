from django.db import models

# Create your models here.

class Contact(models.Model):
    yourName = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.yourName


class Destination(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default = 50000)
    days = models.IntegerField(default=1)
    desc = models.TextField()
    offer = models.BooleanField(default=False)
    img1=models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    img3 = models.ImageField(upload_to='pics')
    day1= models.CharField(max_length=200, blank=True, null=True)
    day2 = models.CharField(max_length=200, blank=True, null=True)
    day3 = models.CharField(max_length=200, blank=True, null=True)
    day4 = models.CharField(max_length=200, blank=True, null=True)
    day5 = models.CharField(max_length=200, blank=True, null=True)
    day6 = models.CharField(max_length=200, blank=True, null=True)
    day7 = models.CharField(max_length=200, blank=True, null=True)
    day8 = models.CharField(max_length=200, blank=True, null=True)
    day9 = models.CharField(max_length=200, blank=True, null=True)
    day10 = models.CharField(max_length=200, blank=True, null=True)
    day11 = models.CharField(max_length=200, blank=True, null=True)
    day12 = models.CharField(max_length=200, blank=True, null=True)
    day13 = models.CharField(max_length=200, blank=True, null=True)
    day14 = models.CharField(max_length=200, blank=True, null=True)
    day15 = models.CharField(max_length=200, blank=True, null=True)
    day16 = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class ConfirmBooking(models.Model):
    fullName = models.CharField(max_length=200,default="")
    fromCity = models.CharField(max_length=100)
    toCity = models.CharField(max_length=100)
    depatureDate = models.DateField()
    days = models.IntegerField(default=1)
    noOfRooms = models.IntegerField()
    noOfAdults = models.IntegerField()
    noOfChildren = models.IntegerField()
    email = models.EmailField(max_length=254)
    phoneNo = models.CharField(max_length=12)
    amountPerPerson = models.IntegerField(default=0)
    totalAmount = models.FloatField(default=0)
    userName = models.CharField(max_length=200, default="")
    date = models.DateField(("Date"), auto_now_add=True)


    def __str__(self):
        return self.fullName

class ott_plans(models.Model):
    url = models.CharField(max_length=200, unique=True, default="", verbose_name="URL (auto generated. Don't touch)")
    name=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=100,default="")
    images=models.ImageField(upload_to='pics')
    f1 = models.CharField(max_length=100)
    f2 = models.CharField(max_length=100)
    f3 = models.CharField(max_length=100)
    f4 = models.CharField(max_length=100)
    added_desc=models.CharField(max_length=300)
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class netflix(models.Model):
    name=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=100,default="")
    images=models.ImageField(upload_to='netflix')
    ratings=models.CharField(max_length=100,default="")
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class amazon(models.Model):
    name=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=100,default="")
    images=models.ImageField(upload_to='amazon')
    ratings=models.CharField(max_length=100,default="")
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class hotstar(models.Model):
    name=models.CharField(max_length=100,default="")
    description=models.CharField(max_length=100,default="")
    images=models.ImageField(upload_to='hotstar')
    ratings=models.CharField(max_length=100,default="")
    createdTime = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
