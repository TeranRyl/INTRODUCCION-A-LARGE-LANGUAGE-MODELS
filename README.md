# INTRODUCCION A LLM
Crear una base de datos de vectores en Pinecone Starter Version (https://www.pinecone.io/) usando su correo institucional, cargar los documentos anexos (FAQs de universidades) usando Embeddings de OpenAI y Langchain. Configurar una Tool de langchain que consulte los documentos y genere una respuesta

## Instrucciones para ejecutar

### Paquetes Python

Se deben instalar los modulos contenidos en el archivo de texto `requirements.txt`.
Para ello puede utilizar el comando `pip install` desde su linea de comandos para instalar los
paquetes en su sistema.

![image](https://github.com/TeranRyl/INTRODUCCION-A-LARGE-LANGUAGE-MODELS/assets/81679109/a08765c9-3c0d-4224-9d00-fdbdf2328a60)



### Local

Paso a paso

```
1. Bajar el .ZIP del repositorio.

2. Extraer el archivo comprimido.

3. Abrir el Shell.

4. Desde el Shell, muevase a la ubicacion donde extrajo el archivo .ZIP (Deberia estar dentro de la carpeta llamada  "INTRODUCCION-A-LARGE-LANGUAGE-MODELS-master").

5. Debe configurar las variables de entorno definidas en el programa "basic_tool.py".
```

![image](https://github.com/TeranRyl/INTRODUCCION-A-LARGE-LANGUAGE-MODELS/assets/81679109/803372bd-f639-4693-928c-9ad721153696)


`PINECONE_API_KEY`: Clave API en el agente AI de Pinecone

`PINECONE_ENVIRONMENT`: Ambiente de la clave API en el agente AI de Pinecone. Si esta utilizando Pinecone Starter Version, este valor deberia ser "gcp-starter".

`OPENAI_API_KEY`: Clave API de OpenAI, obtenida de "https://platform.openai.com/account/api-keys"


Para establecer una variable de entorno en la linea de comandos (CMD) utilice el comando "set". Puede tomar de referencia el siguiente ejemplo:

`set PINECONE_ENVIRONMENT="gcp-starter"`

```
6. Escriba Python basic_tool.py para ejecutar el script.

7. El sistema le pedira que escriba una consulta relacionada al FAQS de algunos programas de la universidad Escuela Colombiana de Ingenieria Julio Garavito. Puede preguntar algo parecido a:
```

`¿Cuantos años de acreditación tiene ingeniería de industrial?`



## Evaluacion

Al ejecutar el script Python deberia ver algo asi:

![image](https://github.com/TeranRyl/INTRODUCCION-A-LARGE-LANGUAGE-MODELS/assets/81679109/a919dc67-4144-474c-9830-3b955380981a)

No se pudieron hacer mas pruebas debido a que la clave de OpenAI fue borrada.




## Implementacion

### Arquitectura

### Pinecone

#### Clave API en el agente AI

![image](https://github.com/TeranRyl/INTRODUCCION-A-LARGE-LANGUAGE-MODELS/assets/81679109/c77a6f3a-4afb-415d-a291-73c259f554f8)

### Base de datos de vectores en el agente AI

![image](https://github.com/TeranRyl/INTRODUCCION-A-LARGE-LANGUAGE-MODELS/assets/81679109/0bf46fef-fd36-4b29-bf9a-f4c9295a4003)


## Construido con

* [Python](https://www.python.org/) - Lenguaje de programacion
* [Git/Github](https://git-scm.com/) - Control de versiones
* [IntelliJ IDEA](https://www.jetbrains.com/idea/) - IDE 

## Autores

* **Juan Francisco Teran** - *Trabajo total* - [TeranRyl](https://github.com/TeranRyl)

## Licencia

Este proyecto tiene la licencia GNU General Public License v3.0; consulte el archivo [LICENSE](LICENSE.txt) para obtener más información.

## Reconocimientos

* PurpleBooth - Plantilla para hacer un buen README
* Luis Daniel Benavides - Preparacion para el taller
* Sainapsis - Preparacion para el taller

