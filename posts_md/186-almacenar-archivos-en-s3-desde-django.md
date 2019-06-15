Title: Almacenar Archivos en S3 desde Django
Date: 2017-11-30T17:49:15+00:00
Description: Como guardar archivos en S3 usando Django
Tags: Django,AWS,S3
---
# Almacenar Archivos en S3 desde DjangoA pesar de que [ya existe un post similar](http://blog.contraslash.com/archivos-estaticos-en-s3-con-django/), hago necesario escribir la versión condensada para alojar archivos en S3 usando Django.

TL;DR

1. Cree un bucket en S3
2. Cree un usuario IAM
3. Pegue esto en la politica del bucket modificando los valores correspondientes

  ```
    {
        "Statement": [
            {
              "Sid":"PublicReadForGetBucketObjects",
              "Effect":"Allow",
              "Principal": {
                    "AWS": "*"
                 },
              "Action":["s3:GetObject"],
              "Resource":["arn:aws:s3:::<BUCKET_NAME>/*"
              ]
            },
            {
                "Action": "s3:*",
                "Effect": "Allow",
                "Resource": [
                    "arn:aws:s3:::<BUCKET_NAME>",
                    "arn:aws:s3:::<BUCKET_NAME>/*"
                ],
                "Principal": {
                    "AWS": [
                        "<USER_ARN>"
                    ]
                }
            }
        ]
    }
  ```
1. Instale
  
  ```
  pip install django-storages boto3
  ```
1.  Cree un archivo en la carpeta del proyecto, al lado de `settings.py` llamada `custom_storages.py` y añadale este contenido:
  ```
from django.conf import LazySettings
    from storages.backends.s3boto3 import S3Boto3Storage
    
    settings = LazySettings()
    
    
    class MediaStorage(S3Boto3Storage):
        location = ""
        bucket_name = settings.AWS_MEDIA_STORAGE_BUCKET_NAME
        access_key = settings.AWS_MEDIA_ACCESS_KEY_ID
        secret_key = settings.AWS_MEDIA_SECRET_ACCESS_KEY
        region_name = settings.AWS_MEDIA_S3_REGION_NAME
        custom_domain = settings.AWS_MEDIA_S3_CUSTOM_DOMAIN

  ```
1. Al final del archivo de `settings.py` incluya esto reemplazando por los valores correctos

  ```
    AWS_MEDIA_STORAGE_BUCKET_NAME = '<BUCKET_NAME>'
    AWS_MEDIA_S3_REGION_NAME = '<AWS_REGION>'
    AWS_MEDIA_ACCESS_KEY_ID = '<SECRET_IAM_KEY_ID>'
    AWS_MEDIA_SECRET_ACCESS_KEY = '<SECRET_IAM_ACCESS_ID>'
    AWS_MEDIA_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS
    DEFAULT_FILE_STORAGE = '<PROJECT_NAME>.custom_storages.MediaStorage'
  ```