def article_validate(task_name, description, status):
    errors = {}
    if not task_name:
        errors["task_name"] = "Поле обязательное"
    elif len(task_name) > 50:
        errors["title"] = "Должно быть меньше 50 символов"
    if not description:
        errors["description"] = "Поле обязательное"
    elif len(description) > 3000:
        errors["description"] = "Должно быть меньше 3000 символов"
    if not status:
        errors["status"] = "Поле обязательное"
    elif len(status) > 60:
        errors["status"] = "Должно быть меньше 60 символов"
    return errors
