from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Characters(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Quotes(models.Model):
    text = models.TextField()
    character = models.ForeignKey(Characters, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Characters, on_delete=models.CASCADE, null=True, blank=True)
    quote = models.ForeignKey(Quotes, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
