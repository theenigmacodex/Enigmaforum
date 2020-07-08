from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import random
random_bios = ["Hey, I am new to Ace Students","Hello people","This is fun","I really need to change my bio"]


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default_female.png',upload_to='profile_pics')
    bg_img = models.ImageField(default='defpfpbck.png',upload_to='bg_profile_pic')
    bio = models.TextField(default=random.choice(random_bios))
    is_faculty = models.BooleanField(default=False)
    pro_user = models.BooleanField(default=False)
    github = models.CharField(max_length=200,verbose_name='Github',blank=True)
    comp_prog = models.URLField(max_length=200,verbose_name='Competitve Coding',help_text='Any Competitve programming profile (ProjectEuler, Hackerrank , Hackerearth ...)',blank=True)
    def __str__(self):
        return f'{self.user}'
    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if(not self.pro_user):
            img.thumbnail((300,300))
            img.save(self.image.path)


