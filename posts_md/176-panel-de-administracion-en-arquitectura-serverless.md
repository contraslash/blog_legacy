Title: Panel de administración en arquitectura Serverless usando servicios de AWS
Date: 2017-07-13T23:44:23+00:00
Description: Panel de administración en arquitectura Serverless usando servicios de AWS
Tags: AWS,serverless
---
# Panel de administración en arquitectura Serverless usando servicios de AWS> [Original](https://medium.com/@contraslash/panel-de-administraci%C3%B3n-en-arquitectura-serverless-usando-servicios-de-aws-7602204fe904)

No puedo decir con exactitud cuando nacieron las arquitecturas serverless, se que después del PaaS (Platform as a Service) llegaron servicios de BaaS (Backend as a Service) popularizándose grandemente con Parse y Firebase, y de repente, teníamos a Amazon promocionando Lambda y a Googleazure y Microsoft haciendo lo suyo.

Aunque debo aceptar que nunca he sido muy fan de AWS, cuando escuché sobre Lambda y sus ambiciones, la idea loca de tener aplicaciones completas sin tener que preocuparse por infraestructura, pero al mismo tiempo preocupándose por todas las dependencias de código y responsabilizándose por una buena adhesión entre componentes aislados me llamó mucho la atención.

Con un amigo había discutido muchas veces sobre en realidad que son las arquitecturas orientadas a microservicios, entre las cosas que le decía le decía que para mi lo único importante era mantener las entradas y salidas limpias. Un requerimiento mas bien pragmático pero vitalísimo a la hora de manejar concurrencia y paralelizaciones.

Este post está altamente basado en un post único de Richard Freeman, el cual aunque no usa Lambda directamente, estructura las bases necesarias para tener una aplicación 100% serverless.
La idea principal aquí es alojar nuestro sitio en S3, manejar la identidad con Cognito y almacenar información con Dynamo.
No voy a ahondar con pantallazos, pues si algo he visto es que los páneles de administración cambiar mucho con el tiempo, pero las URL (al menos de los sitios responsables), se mantienen con el tiempo.
También antes de continuar les enlazo el código fuente, previamente limpiado de identificadores que se relaciones con mi cuenta de AWS y el showcase, que espero también pueda permanecer en el tiempo.

Como primera instancia debemos crear un nuevo Bucket y configurarlo para que aloje una página web, para ellos tenemos la documentación oficial.

En lo personal, para subir los archivos desde mi carpeta de trabajo, uso la Interfaz de Linea de Comandos (CLI) de amazon que es fácilmente instalable usando pip.

```
pip install awscli
```

Para configurarla recomiendo de nuevo seguir el tutorial oficial
El comando de sincronización es algo como

```
aws s3 sync . s3://<tu_nombre_de_bucket>
```

Importante que tu rol IAM tenga permisos de escritura sobre el bucket o tendrás muchos errores 403 en tu línea de comandos
Otro asunto importante es dar permisos públicos a todos los archivos, de lo contrario tendrás mas errores 403, pero ahora en tu navegador.

Con los archivos estáticos listos para ser servidos, vamos a crear una tabla en Dynamo, tarea que se puede realizar directamente desde la consola webde aws, lastimosamente la documentación de AWS no especifica como crear tablas desde la consola web de AWS, pero no es ciencia de cohetes. Basta con definir un nombre para nuestra llave primaria y crear la tabla.

Si es la primera vez que trabajas con NoSQL y específicamente con Dynamo, notarás que esta es la cosa mas absurda del mundo, pues en el mundo relacional, es muy tradicional que las llaves primarias sean únicas y por lo general se auto incrementen, al igual que las llaves de orden, pero la manera de pensar de Dynamo es muy distinta. Altamente recomiendo leer toda la sección de Introducción a Amazon DynamoDB.

Lo siguiente será configurar Cognito para dar permisos a nuestra base de datos DynamoDB, para ello primero debemos crear un Identity Pool, siguiendo el tutorial oficial, pero antes de terminar, debemos añadir una política de permisos a nuestro rol no autenticado.

Aunque en la foto no se aprecien bien los pasos, espero que de una idea mas clara que si menciono las instrucciones por escrito.
La política de documentos debe tener el siguiente contenido:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "mobileanalytics:PutEvents",
                "cognito-sync:*"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "DynamoDBAccess",
            "Effect": "Allow",
            "Action": [
                "dynamodb:BatchGetItem",
                "dynamodb:DescribeStream",
                "dynamodb:DescribeTable",
                "dynamodb:GetItem",
                "dynamodb:GetRecords",
                "dynamodb:GetShardIterator",
                "dynamodb:ListStreams",
                "dynamodb:Query",
                "dynamodb:Scan"
            ],
            "Resource": [
                "<arn_de_la_tabla_dynamo>"
            ]
        }
    ]
}
```
Asegúrate de incluir el arn completo (y sin los caracteres <>) de tu tabla en DynamoDB, el ARN debería parecerse a esto
`arn:aws:dynamodb:us-east-1:111111111111:table/serverless`
Donde `us-east-1` es la región `111111111111` es el número de cliente y serverless es el nombre de la tabla.

Una vez creado el Identity Pool, podremos obtener su ID que debemos copiar en nuestro código Javascript, el el archivo `js/chart_dashboard.js` en la lína 6 y 22, en la lína 4 debemos especificar la región, que podría ser `us-east-1`.
Aunque aún no implementamos nuestros servicios Lambda para acceder a los datos, esta es una primera aproximación de la capacidad que tienen las arquitecturas serverless.