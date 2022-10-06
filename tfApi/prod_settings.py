from .settings import *
import dj_database_url

TEMPLATE_DEBUG = False
DEBUG = bool(os.environ.get('DEBUG', 'False'))

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

storage_location = os.environ.get("FILES_STORAGE_LOCATION", "cloudinary")

if storage_location == 'cloudinary':

    # tefbasiL2000=
    # tefbasil@gmail.com
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME', 'sh2022'),
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY', '629285214388371'),
        'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET', 'sv7QaY2mSqTc95IbTJkzQcm0ApA'),
    }
