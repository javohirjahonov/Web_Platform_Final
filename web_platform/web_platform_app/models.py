from django.db import models


class ServiceModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='service/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OurTeamModel(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(default='No description')
    image = models.ImageField(upload_to='team/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CountersModel(models.Model):
    title = models.CharField(max_length=100)
    count = models.IntegerField()

    def __str__(self):
        return self.title
