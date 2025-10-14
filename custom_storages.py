from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticFileStorages(S3Boto3Storage):
    location = settings.STATICFILES_FOLDER
    #default_acl = "public-read"
    querystring_auth = False
    file_overwrite = False

class MediaFileStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_FOLDER
    #default_acl = "public-read"
    querystring_auth = False
    file_overwrite = False