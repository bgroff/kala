from django_kala.functions import get_env_variable

S3_MEDIA_URL = get_env_variable('S3_MEDIA_URL', '')
S3_STORAGE_BUCKET = get_env_variable('S3_STORAGE_BUCKET', '')
AWS_REGION = get_env_variable('AWS_REGION', 'us-west-1')
S3_STORAGE_PREFIX = get_env_variable('S3_STORAGE_PREFIX', '')
