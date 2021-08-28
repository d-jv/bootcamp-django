from django.db import models, IntegrityError


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['email']) < 4:
            errors["email"] = "El email de usuario debe tener al menos 4 letras"
        if len(postData['password']) < 6:
            errors["password"] = "La contraseña de usuario debe tener al menos 6 letras"
        if postData['password'] != postData['password_check']:
            errors["password"] = "Ambas contraseñas deben ser iguales"
        return errors
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

class User(models.Model):
    # name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    alllowed = models.BooleanField(default=True)
    avatar = models.URLField(default='https://icon-library.com/images/coder-icon/coder-icon-26.jpg')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    # User Manager 
    objects = UserManager()