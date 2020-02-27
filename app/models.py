from django.db import models

# Create your models here.

class Submissions(models.Model):

    name = models.CharField(max_length=200)
    dish_starter = models.CharField(max_length=100)
    dish_main = models.CharField(max_length=100,blank=True,null=True)
    dish_desert = models.CharField(max_length=100,blank=True,null=True)
    starter = models.TextField(blank=True,null=True)
    main = models.TextField(blank=True,null=True)
    bread = models.TextField(blank=True,null=True)
    desert = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
