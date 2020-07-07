from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import random
random_bios = ["Hey, I am new to Ace Students","Hello people","This is fun","I really need to change my bio"]


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.png',upload_to='profile_pics')
    bg_img = models.ImageField(default='default.png',upload_to='bg_profile_pic')
    bio = models.TextField(default=random.choice(random_bios))
    is_faculty = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user}'

