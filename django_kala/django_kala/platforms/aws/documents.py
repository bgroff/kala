import datetime

from django.conf import settings
from django.utils import timezone
from uuid import uuid4

import boto3


class DocumentHandler():

    def get_document_url(self, document):
        s3 = boto3.client('s3')
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': settings.S3_STORAGE_BUCKET,
                'Key': '{0}/media/documents/{1}'.format(settings.S3_STORAGE_PREFIX, document.uuid),
                'ResponseContentDisposition': 'attachment; filename="{0}"'.format(document.name),
            }
        )
        return url

    def upload_document(self, content, key):
        s3 = boto3.client('s3')
        s3.put_object(
            ACL='private',
            Body=content,
            Bucket=settings.S3_STORAGE_BUCKET,
            Key='{0}/media/documents/{1}'.format(settings.S3_STORAGE_PREFIX, key),
            ServerSideEncryption='AES256',

        )

    def get_export_url(self, export):
        s3 = boto3.client('s3')
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': settings.S3_STORAGE_BUCKET,
                'Key': '{0}'.format(export.details['Key']),
                'ResponseContentDisposition': 'attachment; filename="{0}"'.format(export.name),
            }
        )
        return url

    def upload_export(self, export_path):
        key = '{0}/exports/{1}'.format(settings.S3_STORAGE_PREFIX, uuid4())
        expires = timezone.now() + datetime.timedelta(days=settings.EXPORT_EXPIRATION_IN_DAYS)

        s3 = boto3.resource('s3')
        s3.meta.client.upload_file(
            Filename=export_path,
            Bucket=settings.S3_STORAGE_BUCKET,
            Key=key,
            ExtraArgs={
                'Expires': expires,
                'ServerSideEncryption': 'AES256'
            }
        )

        return {'Key': key}

    def archive_document(self, document):
        raise NotImplementedError()

    def restore_document(self, document):
        raise NotImplementedError()

    def delete_document(self, document):
        s3 = boto3.resource('s3')
        for version in document.documentversion_set.all():
            s3.Object(
                settings.S3_STORAGE_BUCKET,
                '{0}/media/documents/{1}'.format(settings.S3_STORAGE_PREFIX, version.uuid)
            ).delete()
