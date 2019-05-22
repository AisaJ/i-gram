from django.test import TestCase
from  .models Image,Profile
# Create your tests here.

class ImageTestClass(TestCase):
  def setUp(self):
    self.holiday = Image(image='jinja.jpeg',name='jinja',caption='A visit to our neighbouring country',likes='2',comments='Looks adventurous')
    self.holiday.save()

  def test_instance(self):
    self.assetTrue(isinstance(self.holiday,Image))

  def tearDown(self):
    Image.objects.all().delete()

  def image_update(self):
    self.holiday = Image(name='jinja')
    Image.objects.name(name='arusha')
    self.holiday.save()

class ProfileTestClass(TestCase):
  def setUp(self):
    self.Jem = Profile(profile_pic='me.jpeg',bio='Always being awesome!')
    self.Jem.save()

  def test_instance(self):
    self.assertTrue(isinstance(self.Jem,Profile))

  def tearDown(self):
    Profile.objects.all().delete()
