from django.db import models, IntegrityError

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['email']) < 4:
            errors["email"] = "El email de usuario debe tener al menos 4 letras"
        if len(postData['password']) < 5:
            errors["password"] = "La contraseña de usuario debe tener al menos 5 letras"
        if postData['password'] != postData['password_check']:
            errors["password"] = "Ambas contraseñas deben ser iguales"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    alllowed = models.BooleanField(default=True)
    avatar = models.URLField(default='https://icon-library.com/images/coder-icon/coder-icon-26.jpg')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    # User Manager 
    objects = UserManager()
    def __str__(self) -> str:
        return f'{self.id} : {self.first_name} {self.last_name}'

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self) -> str:
        return f'{self.id} : ({self.user}) : {self.message}'


class Comment(models.Model):
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self) -> str:
        return f'{self.id} : ({self.user}) : {self.comment}'
