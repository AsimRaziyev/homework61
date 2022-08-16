from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Profile(models.Model):
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True, verbose_name="Аватар")
    profile_on_github = models.URLField(verbose_name="Ссылка на GitHub", null=True)
    about = models.TextField(verbose_name="О себе", null=True)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                verbose_name="Пользователь", related_name="profile")

    def __str__(self):
        return f"{self.user}"
