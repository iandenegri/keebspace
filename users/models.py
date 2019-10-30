from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

username_validator = UnicodeUsernameValidator()
# Create your models here.

class CustomUser(AbstractUser):
    # Add custom fields here later.

    username = models.CharField(
        _('username'),
        max_length=16,
        unique=True,
        help_text=_('Required. 16 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    date_of_birth = models.DateField(auto_now=False, blank=True, null=True)
    about_me = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)


    def __str__(self):
        return (self.email + " - " + self.username)
