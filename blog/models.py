from django.db import models
from django.utils.timezone import now
import django
from django.template.defaultfilters import truncatewords

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default = django.utils.timezone.now)
    body = models.TextField()
    
    def summary(self):
       return truncatewords(self.body,15)

    def __str__(self) :
       return self.title