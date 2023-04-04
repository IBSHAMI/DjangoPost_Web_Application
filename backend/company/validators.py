from django.core.exceptions import ValidationError


def validate_logo_file_size(value):
    max_file_size = 2 * 1024 * 1024  # 5 MB, change this to the maximum allowed size
    if value.size > max_file_size:
        raise ValidationError(f"The file size must be below {max_file_size / (1024 * 1024)} MB.")
