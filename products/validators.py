import os

from django.core.exceptions import ValidationError


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.jpeg', 'gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_image_size(value):  # add this to some file where you can import it from
    limit = 10 * 1024 * 1024  # 5Mo
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MiB.')


def validate_file_size(value):  # add this to some file where you can import it from
    limit = 50 * 1024 * 1024  # 50Mo
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 50 MiB.')
