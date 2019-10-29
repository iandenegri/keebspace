from django.db import models
from django.utils.timezone import now

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

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.owner:
            return (str(self.name) + " by user: " + str(self.owner.username))
        else:
            return str(self.name)