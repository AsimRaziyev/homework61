import factory.fuzzy

from webapp.models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    summary = factory.Faker("summary")
    author = factory.Faker("author")
    description = factory.Faker("description")
