from django.db import models

# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Task(BaseModel):
    task_name = models.CharField(max_length=50, null=False, verbose_name="Названия задачи")
    description = models.TextField(max_length=3000, null=False, verbose_name="Описание")
    status = models.CharField(max_length=60, null=False, verbose_name="Статус", default=STATUS_CHOICES,
                              choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.id}. {self.description}: {self.status}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Comment(BaseModel):
    text = models.TextField(max_length=400, verbose_name="Комментарий")
    author = models.CharField(max_length=40, null=True, default="Аноним", verbose_name="Автор")
    task = models.ForeignKey("webapp.Task", on_delete=models.CASCADE, related_name="comments", verbose_name="Задача")

    def __str__(self):
        return f"{self.id}. {self.text}: {self.author}"

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
