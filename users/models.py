from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    # Add custom fields here later.
    username_validator = UnicodeUsernameValidator()

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
    email = models.EmailField(_('email address'), blank=True, unique=True)


    def __str__(self):
        return (self.email + " - " + self.username)