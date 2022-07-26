from django.db import models
from django.urls import reverse
from webapp.validate import validate_summary, validate_description, validate_author


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Task(BaseModel):
    summary = models.CharField(max_length=100, null=True,
                               verbose_name="Pезюме", validators=[validate_summary])
    author = models.CharField(max_length=50, verbose_name="Автор", default="Unknown", validators=[validate_author])
    description = models.TextField(max_length=3000, null=True,
                                   verbose_name="Описание", validators=[validate_description])
    status = models.ForeignKey("webapp.Statuses", null=True, on_delete=models.PROTECT,
                               related_name="status", verbose_name="Статус")
    tags = models.ManyToManyField("webapp.Tag", related_name="tasks", blank=True)
    types = models.ManyToManyField("webapp.Types", related_name="tasks", blank=True)
    project = models.ForeignKey("webapp.Project", null=True, on_delete=models.PROTECT,
                               related_name="project", verbose_name="Проект", default=1)

    def __str__(self):
        return f"{self.id}. {self.summary}: {self.author}.{self.description}"

    def get_absolute_url(self):
        return reverse("task_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Comment(BaseModel):
    text = models.TextField(max_length=400, verbose_name="Комментарий")
    author = models.CharField(max_length=40, null=True, default="Аноним", verbose_name="Автор")
    task = models.ForeignKey("webapp.Task", on_delete=models.CASCADE, related_name="comments", verbose_name="Задача")

    def __str__(self):
        return f"{self.id}. {self.text}: {self.author}.{self.task}"

    class Meta:
        db_table = "comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Statuses(BaseModel):
    status_text = models.CharField(max_length=50, null=True, verbose_name="Статус")

    def __str__(self):
        return f"{self.id}. {self.status_text}"

    class Meta:
        db_table = "status"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Types(BaseModel):
    type_text = models.CharField(max_length=50, null=True, verbose_name="Текст")


    def __str__(self):
        return f"{self.id}. {self.type_text}"

    class Meta:
        db_table = "type"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class Tag(BaseModel):
    name = models.CharField(max_length=31, verbose_name='Тэг')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "tags"
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Project(models.Model):
    start_date = models.DateField(verbose_name="Дата создания")
    end_date = models.DateField(verbose_name="Дата окончания", blank=True, null=True)
    name = models.CharField(verbose_name="Имя", max_length=50)
    description = models.TextField(verbose_name="Описание")