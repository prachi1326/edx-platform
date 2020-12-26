from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.PROTECT)
    mobile_no = models.CharField(validators=[phone_regex],
        verbose_name="Mobile Number",
        max_length=15,
    )

    def __str__(self):

        return user.username