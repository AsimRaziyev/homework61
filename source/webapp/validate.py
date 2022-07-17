from django.core.exceptions import ValidationError


def validate_summary(value):
    if len(value) > 7:
        raise ValidationError("Название должно быть короче 7 символов")
    return value


def validate_description(value):
    if len(value) > 3000:
        raise ValidationError("Текст должен содержать до 3000 символов")
    return value