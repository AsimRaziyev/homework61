def article_validate(summary, description):
    errors = {}
    if not summary:
        errors["summary"] = "Поле обязательное"
    elif len(summary) > 100:
        errors["summary"] = "Должно быть меньше 100 символов"
    if not description:
        errors["description"] = "Поле обязательное"
    elif len(description) > 3000:
        errors["description"] = "Должно быть меньше 3000 символов"
    return errors
