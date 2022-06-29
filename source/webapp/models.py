from django.db import models


# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=3000, null=False, verbose_name="Описание")
    status = models.CharField(max_length=100, null=False, verbose_name="Статус", default="New")
    created_at = models.DateField(auto_now_add=True, blank=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.id}. {self.description}: {self.status}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
