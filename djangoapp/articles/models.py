from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 #specyfiing the tpye of our fields
class Article(models.Model): 
    title=  models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default="default.png", blank=True) #it can be  blank filed
    author =models.ForeignKey(User, on_delete = models.PROTECT, default = None)


    #defing how ist gonna look
    #
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50] + '...'
        
#if the field is created it will automatically initialize the value
#add in thumbnail later and also add author later
#todo make migration so that this model is mapped to  database table
#now making migration file which tracks any changes made to a model

#everytiem we make changes to our models we need to run
#python manage.py makemigrations
#python manage.py migrate