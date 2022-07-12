import factory.fuzzy

from webapp.models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    summary = factory.Faker("summary")
    description = factory.Faker("description")
