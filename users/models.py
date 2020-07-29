from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class profile(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __init__(self, arg):
        super(profile, self).__init__()
        self.arg = arg

    def __str__(self):
        return f'{self.user.username}s Profile'
        