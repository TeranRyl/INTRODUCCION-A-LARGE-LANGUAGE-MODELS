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

4. Desde el Shell, muevase a la ubicacion donde extrajo el archivo .ZIP (Deberia estar dentro de la carpeta llamada  "AREP-PARCIAL2-master").

5. Escriba "mvn clean install".

6. Escriba java -cp "target/classes;target/dependency/* co.edu.escuelaing.app.Collatz

   Si tiene linux, debe reemplazar ";" por ":".

7. Abra su navegador web de y busque en una pestaña incognita:
   
   - "localhost:4567" - Cliente web.
   - "localhost:4567/collatz?value=*numero a calcular collatz*" - Servicio GET

```



## Evaluacion

Pruebas de app web funcionando:

Cliente web desde Docker:




Servicio GET desde Docker:




Prueba de demostracion de despliegue de la aplicacion web realizada utilizando EC2 (AWS):



## Implementacion

### Arquitectura


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

