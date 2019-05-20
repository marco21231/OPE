from django.db import models

# Create your models here.
class Index(models.Model):
    waist = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

def __unicode__(self):
    return "{0} {1} {2}".format(
        self, self.waist, self.height)
