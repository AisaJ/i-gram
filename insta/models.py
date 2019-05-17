from django.db import models

# Create your models here.
class Profile(models.Model):
  profile_pic = models.ImageField(upload_to='image/',default='me.png')
  bio = models.TextField()

  def __str__(self):
    return self.bio

class Image(models.Model):
  image = models.ImageField(upload_to='image/',default='arusha.jpeg')
  name = models.CharField(max_length=40)
  caption = models.TextField()
  profile = models.ForeignKey(Profile)
  likes = models.IntegerField()
  comments = models.TextField()

  def __str__(self):
    return self.name
