Title: Archivos estáticos en S3 con Django
Date: 2017-09-05T20:37:55+00:00
Description: Cómo utilizar AWS S3 para servir archivos estáticos con Django
Tags: Django,AWS,S3
---
# Archivos estáticos en S3 con DjangoDebo confesar que tenía una deuda técnica con el blog desde hace un par de meses por no haber traducido oportunamente [este post](https://www.caktusgroup.com/blog/2014/11/10/Using-Amazon-S3-to-store-your-Django-sites-static-and-media-files/). Afortunadamente aún estamos a tiempo.

Como primera instancia necesitaremos [crear un Bucket en S3](http://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

Segundo vamos a crear un [usuario en IAM](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_cliwpsapi), recordemos que necesitaremos un API KEY y un API SECRET, por tanto debemos crear un `acceso programático`.

> Asegúrate de guardar estos valores en un lugar donde no los pierdas.

Una vez creado tu usuario, obtén el ARN, que debe verse algo como 

```
arn:aws:iam::123456789012:user/nombredeusuario
```

Ahora con este ARN en mente debemos [editar la política del bucket S3](http://docs.aws.amazon.com/AmazonS3/latest/user-guide/add-bucket-policy.html) con algo similar a esto.

> Recuerda que debes cambiar los valores entre <> y que los caracteres < y > NO VAN

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

Ahora necesitaremos instalar boto y storages, las librerías que harán la magia de guardado en S3:

```
pip install django-storages boto
```

Añadimos `storages` a nuestro `INSTALLED_APPS` en `settings.py`

```
INSTALLED_APPS = [
      ...
      'storages',
]
```

Y al final de nuestro archivo de configuración `settings.py` añadimos las siguientes líneas reemplazando con los valores apropiados 

```
AWS_ACCESS_KEY_ID = '<ACCESS_KEY>'
AWS_SECRET_ACCESS_KEY = '<SECRET_KEY>'
AWS_STORAGE_BUCKET_NAME = '<NOMBRE_BUCKET>'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
```

Y ya podremos ejecutar con traquilidad

```
python manage.py collectstatic
```