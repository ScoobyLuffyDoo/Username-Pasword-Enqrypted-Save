from django.db import models

class EncryptedDetails(models.Model):
    usernumber =models.CharField(max_length=100)
    username =models.CharField(max_length=10000)
    password = models.CharField(max_length=10000)
    link = models.CharField(max_length=10000)

    # def __str__(self):
    #     return self.username

class UserDetails(models.Model):
    usernumber =models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    userPassword = models.CharField(max_length=500)

    # def __str__(self):
    #     return self.userlink
            