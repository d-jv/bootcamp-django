from django.db import models, IntegrityError

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Network(models.Model):
    name = models.CharField(max_length=255, unique=True)
    shows = models.ManyToManyField(Show, related_name='networks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

