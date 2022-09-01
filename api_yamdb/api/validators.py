from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    if value > timezone.now().year:
        raise ValidationError(
            f'{value} не правильно указан год'
        )


def validate_score(value):
    """Проверка. Оценка в допустимом диапазоне."""

    if (value < 1) or (value > 10):
        raise ValidationError(
            'Оценка должна быть от 1 до 10!'
        )
