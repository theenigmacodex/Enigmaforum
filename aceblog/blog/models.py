from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tag = models.CharField(max_length=20,default='general')
    postimg = models.ImageField(default='defback.png',upload_to='post_pics',verbose_name='Post Image',blank=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    microtext = models.CharField(max_length=20,default='Entry by me',blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    githubrepo = models.CharField(max_length=200,verbose_name="Github repo",blank=True,help_text="Supported User/User-Repo")
    created_date = models.DateTimeField(default=timezone.now)
    commentimg = models.ImageField(default='',upload_to='comment_img',verbose_name='Comment Image')

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.microtext