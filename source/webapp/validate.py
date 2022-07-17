from django.core.exceptions import ValidationError
# def article_validate(summary, description):
#     errors = {}
#     if not summary:
#         errors["summary"] = "Поле обязательное"
#     elif len(summary) > 100:
#         errors["summary"] = "Должно быть меньше 100 символов"
#     if not description:
#         errors["description"] = "Поле обязательное"
#     elif len(description) > 3000:
#         errors["description"] = "Должно быть меньше 3000 символов"
#     return errors


def validate_summary(value):
    if len(value) > 7:
        raise ValidationError("Название должно быть короче 7 символов")
    return value
