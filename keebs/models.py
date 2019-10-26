from django.db import models
from users.models import CustomUser

# Create your models here.

class Build(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    owner = models.ForeignKey(CustomUser, 
                              related_name="builds",  
                              on_delete=models.DO_NOTHING, 
                              blank=True, 
                              null=True)