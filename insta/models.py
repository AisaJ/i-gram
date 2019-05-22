from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
  profile_pic = models.ImageField(upload_to='profile/',default='wink.png')
  bio = models.TextField()
  user = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.bio

  def profile_save(self):
    self.save()

  def profile_delete(self):
    self.delete()
  class Meta:
    ordering=['-bio']

  @classmethod
  def filter_by_username(cls,user_id):
    user = cls.objects.filter(Profile__user=user.id)
    return user

class Image(models.Model):
  image = models.ImageField(upload_to='image/',default='arusha.jpeg')
  name = models.CharField(max_length=40)
  caption = HTMLField()
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  likes = models.IntegerField(default=0)
  comments = HTMLField()
    
  def __str__(self):
    return self.name

  def image_save(self):
    self.save()

  def image_delete(self):
    self.delete()
