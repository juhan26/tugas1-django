from django.db import models

# Create your models here.

class MyProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title

class GuestBook(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title